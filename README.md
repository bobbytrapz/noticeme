# noticeme v2018.12

Provides python bindings for inotify utilizing coroutines.
I wrote this back when I was curious about coroutines but I have been using it lately so I decided to share it.
Please note this only runs on Linux and a have no plans to support any other OS.
There are many, many alternatives though.

## Example

```
import asyncio
import noticeme

@noticeme.watcher('/path/to/directory', 'created modified')
async def my_watcher(event):
  if '.py' == event.path.suffix.lower():
    proc = await asyncio.create_subprocess_exec('cmd', event.path.absolute())
    await proc.wait()

if __name__ == '__main__':
  noticeme.run()
```

Watch '/path/to/directory'. Anytime a file is created or modified we check if
it has '.py' extension. If it does we run 'cmd' with the path of the file as
the first argument.

## Requirements

- Linux >= 2.6.13
- Python >= 3.5
- cffi
- C compiler installed (if you need to run inotify_build.py)

## Install

### Include directly

- Copy noticeme.py and inotify_build.py to your project directory
- Within your project directory run:

```
python3 inotify_build.py
```

- this creates a 'build' directory containing the result of ffibuilder.compile
- You should now be able to use noticeme.
- inotify_build.py will no longer be needed.

### pip

```
pip install --user noticeme
```

## Troubleshooting

- Error: ImportError: No module named '\_inotify'
- Make sure you have a C compiler installed and run:

```
 python3 inotify_build.py
```

## Alternatives

[watchdog](https://github.com/gorakhargosh/watchdog)
[pyinotify](https://github.com/seb-m/pyinotify)

## noticeme cli

If you need a lightweight watcher for a project you can try this.

```
pip install --user noticeme # install
touch noticeme.cfg # edit the config file
noticeme # start watching
```

To see a full list of events:

```
  noticeme events
```

```
# noticeme.cfg
[should]
  clear_screen = no
  clear_after = 0

[imports]
  example = A .py file with a @noticeme.watcher decorator in it

[my_watcher]
  description = This is an example.
  paths = . **
  events = written
  # match any path that starts with docs
  re = ^docs
  glob = *.txt
  shell = echo "test_written: file was added"
```
