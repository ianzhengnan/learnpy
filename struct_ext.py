
import struct, io

def get_file_data(file_path):

    pic = io.open(file_path, 'rb')

    pic_cont = pic.read()
    pic.close()

    return pic_cont[:30]

def print_pic_cont(s):

    pic_cont = struct.unpack('<ccIIIIIIHH', s)

    print(pic_cont)

    if (pic_cont[0] + pic_cont[1]) == b'BM':
        print('It is a bmp picture.')
    else:
        print('It is not a bmp picture.')

# test
file_path = 'test.bmp'
picture_content = get_file_data(file_path)
print_pic_cont(picture_content)