# LogTailTool

LogTailTool tail a log file in python.

## Usage

```python
from logtailtool import LogTailTool

lines = LogTailTool("name.log")
for line in lines:
    print(line)
```
