# File Access Logger

The plan for this script to find when I last looked at a file

Operating systems like Windows make it really easy to see when you last edited a file but not so easy to find out when you last viewed it

This is a pretty simple script that generates a CSV in this format

| Row 1     | Row 2         | Row 3     |
| --------- | ------------- | --------- |
| File Name | Formated time | Unix Time |

## Running the Script

Super simple, all you need to do to run this script is this:

```python
python3 get_details.py <path to directory to scan>
```

### Notes

This is wrote for Python3