from tkinter import *
from PIL import Image, ImageTk

class Triangle:
    def __init__(self, sides, angles):
        self.sides = sides
        self.angles = angles
        self.area = self.area()
        self.perimeter = self.Perimeter_Calculator()

    def istriangle(self):
        return (
            (self.sides[0] + self.sides[1] > self.sides[2]
            and self.sides[1] + self.sides[2] > self.sides[0]
            and self.sides[0] + self.sides[2] > self.sides[1])
            and sum(self.angles) == 180
        )

    def Perimeter_Calculator(self):
        if self.istriangle():
            perimeter = sum(self.sides)
            return perimeter
        else:
            return None

    def IsRightAngled(self):
        return any(angle == 90 for angle in self.angles)

    def area(self):
        if self.istriangle() and self.IsRightAngled():
            return self.Right_Area_Calculator()
        elif self.istriangle() and not self.IsRightAngled():
            return self.Heron_Area_Calculator()
        elif self.invalid():
            return None

    def Right_Area_Calculator(self):
        temp = self.sides.copy()
        max_side = max(temp)
        temp.remove(max_side)
        return (1 / 2) * temp[0] * temp[1]

    def Heron_Area_Calculator(self):
        semi = sum(self.sides) / 2
        heronarea = (semi - self.sides[0]) * (semi - self.sides[1]) * (semi - self.sides[2]) ** 0.5
        return heronarea

    def invalid(self):
        if self.istriangle() == False:
            return True

def label_creator(n):
    ButFrame1 = Frame(ButFrame, borderwidth=3, relief=SUNKEN)
    ButFrame1.grid(row=4 + n, column=0, sticky="new")

    TrLabel = Label(ButFrame1, text="Details of Triangle {i}".format(i=n + 1), font=("Segoe UI", 12), foreground="black")
    TrLabel.grid(row=1 + n, column=0)

    sideframe = Frame(ButFrame1, borderwidth=3, relief=GROOVE)
    sideframe.grid(row=2 + n, column=0)
    sidelist = []
    for i in range(3):
        side = Label(sideframe, text="Side {n}".format(n=i + 1), font=("Segoe UI", 11), foreground="black")
        side.grid(row=i, column=0, sticky="n")
        sideentry = Entry(sideframe)
        sideentry.grid(row=i, column=1, sticky="n")
        sidelist.append(sideentry)

    AngleFrame = Frame(ButFrame1, borderwidth=3, relief=GROOVE)
    AngleFrame.grid(row=2 + n, column=1, sticky="n")
    angleslist = []
    for j in range(3):
        angle = Label(AngleFrame, text="Angle {n}".format(n=j + 1), font=("Segoe UI", 11), foreground="black")
        angle.grid(row=j, column=0, sticky="n")
        angleentry = Entry(AngleFrame)
        angleentry.grid(row=j, column=1, sticky="n")
        angleslist.append(angleentry)

    def data_submit(Triangle, temp):
        answer_frame = Frame(ButFrame1, borderwidth=3, relief=SUNKEN, background="white")
        answer_frame.grid(row=2 + temp, column=4, sticky="nwes")
        if Triangle.invalid() == True:
            Answer = Label(
                answer_frame,
                text="The dimensions of the triangle are invalid. Therefore the area and perimeter cannot be calculated.",
                font=("Segoe UI", 12),
                background="white",
            )
            Answer.grid(row=0, column=0, sticky="nwes")
        else:
            elements = ["sides", "angles"]
            values = [Triangle.sides, Triangle.angles]
            element = ["perimeter", "area"]
            value = [
                f"{Triangle.perimeter} centimeters" if Triangle.perimeter is not None else "N/A",
                f"{Triangle.area} centimeter square" if Triangle.area is not None else "N/A",
            ]
            for i in range(2):
                label = Label(
                    answer_frame, text=f"The {elements[i]} of the triangle are {values[i]}", font=("Segoe UI", 12)
                ,background="white")
                label.grid(row=i, column=0, sticky="nwes")
            for i in range(2):
                label = Label(answer_frame, text=f"The {element[i]} of the triangle is {value[i]}", font=("Segoe UI", 12),background="white")
                label.grid(row=2 + i, column=0, sticky="news")

    Butbutframe = Frame(ButFrame1, borderwidth=3, relief=GROOVE)
    Butbutframe.grid(row=2 + n, column=2, sticky="n")
    temp = int(n)
    Submit = Button(
        Butbutframe,
        text="Submit",
        height=1,
        width=5,
        foreground="black",
        command=lambda: data_submit(
            Triangle([float(entry.get()) for entry in sidelist], [float(entry.get()) for entry in angleslist]), temp
        ),
    )
    Submit.grid(row=0, column=0)

def submit():
    n = int(TriEntry.get())
    for i in range(n):
        label_creator(i)

# GUI setup
root = Tk()
root.title("Triangle Geometry Calculator")
root.geometry("1366x768")
root.minsize(300, 300)
root.columnconfigure(0, weight=1)

frame_label1 = Frame(root, background="dark grey", borderwidth=3, relief=GROOVE)
frame_label1.grid(row=0, column=0, sticky="news")

image = Image.open("no-bg-resize.png")
photo = ImageTk.PhotoImage(image)
photo_label = Label(frame_label1, image=photo)
photo_label.image = photo
photo_label.pack(side="left", anchor="n", padx=(0, 0), pady=(5, 5))

heading1 = Label(frame_label1, text="Triangle Geometry", background="dark grey", font=("Segoe UI", 15,"bold"), foreground="black")
heading1.pack(side="top", anchor="nw", padx=(0, 0), pady=0)

heading2 = Label(frame_label1, text="Calculator", background="dark grey", font=("Segoe UI", 15, "bold"), foreground="black")
heading2.pack(side="top", anchor="w", padx=(0, 0), pady=0)

frame_label2 = Frame(root, borderwidth=2, relief=SUNKEN)
frame_label2.grid(row=1, column=0, sticky="nsew")

content_label = Label(
    frame_label2,
    text="This is a versatile program in a graphical user interface that can be used to perform geometrical operations on a triangle \nwhose sides and angles are given",
    font=("comicsans ms", 16),
)
content_label.pack(side="top", anchor="w", padx=0, pady=0, fill="x")

frame_rules = Frame(root, borderwidth=4, relief=GROOVE)
frame_rules.grid(row=2, column=0, sticky="nwes")

rule = Label(
    frame_rules,
    text="To Start, Simply enter the number of triangles you want to work with..",
    font=("Segoe UI", 13, "bold"),
    foreground="black",
)
rule.pack()

ButFrame = Frame(root, borderwidth=4, relief=GROOVE)
ButFrame.grid(row=3, column=0, sticky="nesw")

TriLabel = Label(ButFrame, text="Number of triangles", font=("Segoe UI", 12, "bold"), foreground="black")
TriLabel.grid(row=0, column=0)

TriEntry = Entry(ButFrame)
TriEntry.grid(row=0, column=1)

numtribut = Button(ButFrame, text="Enter", height=2, width=5, foreground="black", command=submit)
numtribut.grid(row=0, column=2)

mainloop()
