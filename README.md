# Pyreducer : Python work reducer 
Pyreducer is Python work reducer package for reduce the complexity of common task

## Installation :
```bash
    pip install Pyreducer
```
 ## how to use :

 #### Create a new log File
```python
    from pyreducer import write_log
    write_log('Log File Heading',Fresh=False)
```

 #### Append to existing log File
 Example For Str content
```python
    from pyreducer import write_log
    write_log('content to the log ')
```
 Example For Dict content
```python
    from pyreducer import write_log
    write_log({'ID':12311,'status':True})
```