import glob


def save(filename, list):
    with open(filename, 'w', encoding='UTF-8') as f:
        for img in list:
            img = img.replace("\\", "/")
            f.write(img+'\n')

if __name__ == '__main__':
    train_list = glob.glob('data/obj/*.jpg' ,recursive=False)
    test_list = glob.glob('data/test/*.jpg' ,recursive=False)
    
    trainfile = 'data/train.txt'
    testfile = 'data/test.txt'
    save(trainfile, train_list)
    save(testfile, test_list)