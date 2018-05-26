TEMPLATE = aux
OTHER_FILES = \
        diff/ \
        patch/ \
        rpm/ \
        src/

src.path = /usr/share/maliit/plugins/com/jolla

patch.files = patch/*
patch.path = /usr/share/patchmanager/patches/bigger-spacebar

original = original$${src.path}/
patched = patched$${src.path}/

system((cd diff; diff -uprN $$original $$patched) > patch/unified_diff.patch)

INSTALLS += \
        src \
        patch
