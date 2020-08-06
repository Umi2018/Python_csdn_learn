from removebg import RemoveBg

rmbg = RemoveBg('GiQrvx9AuuS6DH2Svh3JBfVK', 'error.log')

def remove_bg(img_path):
    rmbg.remove_background_from_img_file(img_path)