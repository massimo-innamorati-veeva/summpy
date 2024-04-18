#!/usr/bin/env python



def tree_encode(obj, encoding="utf-8"):
    type_ = type(obj)
    if type_ == list or type_ == tuple:
        return [tree_encode(e, encoding) for e in obj]
    elif type_ == dict:
        new_obj = dict(
            (tree_encode(k, encoding), tree_encode(v, encoding))
            for k, v in obj.iteritems()
        )
        return new_obj
    else:
        return obj


if __name__ == "__main__":
    pass
