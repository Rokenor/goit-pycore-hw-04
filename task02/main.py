def get_cats_info(path):
    try:
        cats_info = []
        with open(path, 'r', encoding='utf-8') as file:
            cats_data = file.readlines()
            for cat in cats_data:
                cat_raw_data = cat.strip().split(',')
                cat_data = {
                    "id": cat_raw_data[0],
                    "name": cat_raw_data[1],
                    "age": cat_raw_data[2],
                }
                cats_info.append(cat_data)
        
        return cats_info

    except IndexError:
        print('File with cats info damaged')
        return None
    except FileNotFoundError:
        print('File with cats info doesn\'t exist')
        return None
    except:
        print('Unexpected error with file')
        return None

if __name__ == '__main__':
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)