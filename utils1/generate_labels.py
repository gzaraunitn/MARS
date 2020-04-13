from os import listdir, makedirs, system
from os.path import join, exists

class_map = {
    "jogging": "168",
    "punching person (boxing)": "259",
    "push up": "260",
    "clapping": "57",
    "backflip (human)": "0"
}

dataset_path = '../dataset/Kinetics'
train_path = join(dataset_path, 'train')
test_path = join(dataset_path, 'test')

target_train_labels_path = '../dataset/Kinetics_labels/Kinetics_train_labels.txt'
target_test_labels_path = '../dataset/Kinetics_labels/Kinetics_val_labels.txt'
target_train_labels = open(target_train_labels_path, 'w')
target_test_labels = open(target_test_labels_path, 'w')

classes = [c for c in listdir(train_path) if c != 'backflip (human)']
for c in classes:
    c_path = join(train_path, c)
    videos = listdir(c_path)
    for v in videos:
        v_path = join(c_path, v)
        n_frames = len(listdir(v_path))
        v_path = v_path.replace(" ", "BLANK_DELIMITER")
        v_path = '/'.join(v_path.split('/')[3:])
        class_id = class_map[c]
        out_string = '{} {} {}\n'.format(v_path, class_id, n_frames)
        target_train_labels.write(out_string)

classes = [c for c in listdir(test_path) if c != 'backflip (human)']
for c in classes:
    c_path = join(test_path, c)
    videos = listdir(c_path)
    for v in videos:
        v_path = join(c_path, v)
        n_frames = len(listdir(v_path))
        v_path = v_path.replace(" ", "BLANK_DELIMITER")
        v_path = '/'.join(v_path.split('/')[3:])
        class_id = class_map[c]
        out_string = '{} {} {}\n'.format(v_path, class_id, n_frames)
        target_test_labels.write(out_string)

target_train_labels.close()
target_test_labels.close()