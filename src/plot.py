import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from colors import *

def plot(title, points, point1, point2, saveConfig):
    x = []
    y = []
    z = []
    for point in points:
        if len(point) >= 1:
            x.append(point[0])
        if len(point) >= 2:
            y.append(point[1])
        if len(point) >= 3:
            z.append(point[2])

    fig = plt.figure()
    if len(point) <= 3:
        if len(point) == 1:
            y = [0] * len(x)
            plt.scatter(x, y, c='black', alpha=1)
            plt.scatter(point1[0], 0, c='red')
            plt.scatter(point2[0], 0, c='red')
            xLine = [point1[0], point2[0]]
            yLine = [0, 0]
            plt.plot(xLine, yLine, c='red')
            plt.title(title)
        elif len(point) == 2:
            plt.scatter(x, y, c='black', alpha=1)
            plt.scatter(point1[0], point1[1], c='red')
            plt.scatter(point2[0], point2[1], c='red')
            xLine = [point1[0], point2[0]]
            yLine = [point1[1], point2[1]]
            plt.plot(xLine, yLine, c='red')
            plt.title(title)
        elif len(point) == 3:
            ax = fig.add_subplot(111, projection='3d')
            if (point1[0]) in x:
                x.remove(point1[0])
            if (point1[1]) in y:
                y.remove(point1[1])
            if (point1[2]) in z:
                z.remove(point1[2])
            if (point2[0]) in x:
                x.remove(point2[0])
            if (point2[1]) in y:
                y.remove(point2[1])
            if (point2[2]) in z:
                z.remove(point2[2])
            ax.scatter(x, y, z, c='black', alpha=1)
            ax.scatter(point1[0], point1[1], point1[2], c='red')
            ax.scatter(point2[0], point2[1], point2[2], c='red')

            xLine = [point1[0], point2[0]]
            yLine = [point1[1], point2[1]]
            zLine = [point1[2], point2[2]]
            ax.plot(xLine, yLine, zLine, c='red')
            ax.set_title(title)
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')

        if saveConfig is None:
            plt.show()
        else:
            plt.savefig(saveConfig)

    else:
        if saveConfig is None:
            print(WHITE + "Not visualizable!\n" + RESET)
        else:
            img = Image.new('RGB', (640, 480), color = 'white')

            draw = ImageDraw.Draw(img)
            text = "Not visualizable!"
            font = ImageFont.truetype('arial.ttf', size=40)
            text_width, text_height = draw.textsize(text, font)
            x = (img.width - text_width) / 2
            y = (img.height - text_height) / 2
            draw.text((x, y), text, font=font, fill='black')

            img.save(saveConfig)