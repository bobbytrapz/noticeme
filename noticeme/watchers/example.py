import noticeme


@noticeme.watcher('.', 'all all_virtual')
async def test_test(event):
    _dir = event.path.parent
    if event.deleted:
        print("'{}' was deleted from '{}'".format(event.filename, _dir))
    elif event.created:
        print("'{}' was created in '{}'".format(event.filename, _dir))

if __name__ == "__main__":
    noticeme.run()
