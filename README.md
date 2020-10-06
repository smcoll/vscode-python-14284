# steps to reproduce

1. Clone this repo
1. Make and activate a virtual environment at `.venv` (in my case, it's installing as Python 3.8):
   ```
   python3 -m venv .venv
   . .venv/bin/activate
   ```
1. Install requirements
   ```
   pip install -r requirements.txt
   ```
1. Set breakpoints:
   - lines 11 and 13 of `main.py` - _demonstrates debugger working in our module_
   - line 445 of `.venv/lib/python3.8/site-packages/pydantic/main.py` (in `BaseModel.parse_obj`) - _won't break here
   - line 31 of `.venv/lib/python3.8/site-packages/chardet/__init__.py` (in `detect`) - _sanity check demonstrating that breakpoints in installed libs do work in general_
1. Run the "Python: Attach using listen" launch configuration with F5
1. Run the included file:
   ```
   python -m main
   ```

Expected behavior is that the debugger will break at all breakpoints.  The breakpoint in `pydantic` will not work, but the others will.  This example only shows one example of a failing Pydantic breakpoint, but a spot check indicates that it's not isolated to a particular Pydantic module.
