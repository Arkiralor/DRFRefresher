from django.template.defaultfilters import slugify

import uuid

def create_ids():
    id = uuid.uuid1()
    resp_1 = slugify(f"{id}")
    resp_2 = slugify(str(id))
    resp_3 = slugify(id)

    return f"\nfString Slug:\t{resp_1},\nString Slug:\t{resp_2},\nDirect Slug:\t{resp_3}"

def main(n=10):

    for i in range(n):
        print(create_ids())


if __name__=="__main__":
    main(10)


