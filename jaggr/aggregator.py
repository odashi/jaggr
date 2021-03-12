from __future__ import annotations

from typing import Any, Union


def _flatten(data):
  if isinstance(data, (tuple, list)):
    children = [_flatten(d) for d in data]
    values = sum((c[0] for c in children), [])
    schema = type(data)(c[1] for c in children)
    return values, schema
  elif isinstance(data, dict):
    children = [(k, _flatten(d)) for k, d in sorted(data.items())]
    values = sum((c[0] for _, c in children), [])
    schema = {k: c[1] for k, c in children}
    return values, schema
  else:
    return [data], type(data)


def _unflatten(values: list[Any], schema: Any):
  def _unflatten_inner(values, schema, offset):
    if isinstance(schema, (tuple, list)):
      children = []
      for s in schema:
        c, offset = _unflatten_inner(values, s, offset)
        children.append(c)
      return type(schema)(children), offset
    if isinstance(schema, dict):
      children = {}
      for k, s in sorted(schema.items()):
        c, offset = _unflatten_inner(values, s, offset)
        children[k] = c
      return children, offset
    else:
      return schema(values[offset]), offset + 1
  return _unflatten_inner(values, schema, 0)[0]


class Aggregator:
  def __init__(self, data: Any):
    self._data = data

  def _sum(self):
    if isinstance(self._data, (tuple, list)):
      if not self._data:
        return Aggregator(None)
      aggregated, schema = _flatten(self._data[0])
      num_values = len(aggregated)
      for i in range(1, len(self._data)):
        values, s = _flatten(self._data[i])
        if s != schema:
          raise ValueError(f'Schema does not match: {s} != {schema}')
        for j in range(num_values):
          aggregated[j] += values[j]
      return Aggregator(_unflatten(aggregated, schema))

  def __getattr__(self, name: str) -> 'Aggregator':
    if name == '__sum__':
      return self._sum()
    if isinstance(self._data, dict):
      return Aggregator(self._data[name])
    else:
      raise TypeError('data is not a dict.')

  def __getitem__(self, idx: Union[int, str]) -> 'Aggregator':
    if isinstance(self._data, (list, tuple, dict)):
      return Aggregator(self._data[idx])
    else:
      raise TypeError('data is not a sequence.')

  def __str__(self):
    return str(self._data)

  def get(self):
    return self._data
