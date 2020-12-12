# Herbera
Herbera - really light-weight debug lib. It just takes the `sys.modules['__main__']` on `herbera.breakpoint()` call, and recursively displaying it's content
---
# How to use:
  Short example:
  ```
  import herbera
  
  herbera.debug = True  # or False, herbera.breakpoint() calls will be ignored
  
  x = 5
  herbera.breakpoint()
  
  x = 10
  herbera.breakpoint()
  ```

### `herbera.breakpoint()` takes such parameters, as: from_context, output_manager
  #### `from_context` - object with `__dict__` attribute. Main module by default
  #### `output_manager` - callable object, which takes at least one parameter (string). Built-in `print` by default
