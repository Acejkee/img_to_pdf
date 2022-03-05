# https://www.recordpower.co.uk/flip/Winter2020/mobile/index.html

import requests
import img2pdf


def get_data():
    headers = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }

    for i in range(1, 49):
        url = f"https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg"
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f"media/{i}.jpg", "wb") as file:
            file.write(response)
            print(f"Downloaded {i} of 48")


def write_to_pdf():
    img_list = [f"media/{i}.jpg" for i in range(1, 49)]

    #create PDF file
    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))
    print("file result.pdf ready!")


def main():
    #get_data()
    write_to_pdf()



if __name__ == '__main__':
    main()

