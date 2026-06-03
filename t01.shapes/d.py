import math

class Shape:
    def perimeter(self): pass
    def area(self): pass

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = float(a), float(b), float(c)
        if self.a <= 0 or self.b <= 0 or self.c <= 0: raise ValueError
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a: raise ValueError
    def perimeter(self): return self.a + self.b + self.c
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(max(0, p * (p - self.a) * (p - self.b) * (p - self.c)))
    def __str__(self): return f"Triangle({self.a}, {self.b}, {self.c})"

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a, self.b = float(a), float(b)
        if self.a <= 0 or self.b <= 0: raise ValueError
    def perimeter(self): return 2 * (self.a + self.b)
    def area(self): return self.a * self.b
    def __str__(self): return f"Rectangle({self.a}, {self.b})"

class Trapeze(Shape):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = float(a), float(b), float(c), float(d)
        if self.a <= 0 or self.b <= 0 or self.c <= 0 or self.d <= 0 or self.a == self.b: raise ValueError
    def perimeter(self): return self.a + self.b + self.c + self.d
    def area(self):
        diff = abs(self.a - self.b)
        h_squared = self.c**2 - ((diff**2 + self.c**2 - self.d**2) / (2 * diff))**2
        if h_squared <= 0: raise ValueError
        return ((self.a + self.b) / 2) * math.sqrt(h_squared)
    def __str__(self): return f"Trapeze({self.a}, {self.b}, {self.c}, {self.d})"

class Parallelogram(Shape):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = float(a), float(b), float(h)
        if self.a <= 0 or self.b <= 0 or self.h <= 0 or self.h > self.b: raise ValueError
    def perimeter(self): return 2 * (self.a + self.b)
    def area(self): return self.a * self.h
    def __str__(self): return f"Parallelogram({self.a}, {self.b}, {self.h})"

class Circle(Shape):
    def __init__(self, r):
        self.r = float(r)
        if self.r <= 0: raise ValueError
    def perimeter(self): return 2 * math.pi * self.r
    def area(self): return math.pi * (self.r ** 2)
    def __str__(self): return f"Circle({self.r})"

def read_shapes(filename):
    shapes = []
    mapping = {
        "Triangle": Triangle, "Rectangle": Rectangle,
        "Trapeze": Trapeze, "Parallelogram": Parallelogram, "Circle": Circle
    }
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.split()
                if not parts: continue
                name, params = parts[0], parts[1:]
                if name in mapping:
                    try:
                        obj = mapping[name](*params)
                        obj.area()
                        shapes.append(obj)
                    except Exception:
                        continue
        return shapes
    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено.")
        return None

def process_file(filename):
    data = read_shapes(filename)
    if not data:
        return

    m_area = max(data, key=lambda x: x.area())
    m_peri = max(data, key=lambda x: x.perimeter())

    print(f"=== РЕЗУЛЬТАТ ДЛЯ ФАЙЛУ: {filename} ===")
    print(f"Успішно зчитано коректних фігур: {len(data)}")
    print(f"  Max Area:      {m_area} (S = {m_area.area():.2f})")
    print(f"  Max Perimeter: {m_peri} (P = {m_peri.perimeter():.2f})")
    print("-" * 50)

def main():
    files = ["input01.txt", "input02.txt", "input03.txt"]
    for filename in files:
        process_file(filename)

if __name__ == "__main__":
    main()