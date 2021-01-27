# LogTailTool

LogTailTool tail a log file in python.

## Usage (in python code)

```python
from logtailtool import LogTailTool

lines = LogTailTool("name.log")
for line in lines:
    print(line)
```

## Usage (command)

```text
usage: logtailtool.py [-h] -f FILENAME [-p PATTERN] [-b] [-i INTERVAL]

LogTailTool

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --file FILENAME
                        Log file path (required)
  -p PATTERN, --pattern PATTERN
                        Pattern to extract (default: None)
  -b, --read-from-begin
                        Read from the begin of the file (default: false)
  -i INTERVAL, --interval INTERVAL
                        Interval time (default: 1)
```
