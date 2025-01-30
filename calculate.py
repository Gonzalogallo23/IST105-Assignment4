import sys
import math

def calculate(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        if a < 1:
            return "<p style='color: red;'>Input a is too small.</p>"
        if b == 0:
            return "<p style='color: blue;'>b is zero and will not affect the result.</p>"
        if c < 0:
            return "<p style='color: red;'>Error: c cannot be negative.</p>"

        c_cubed = c ** 3
        if c_cubed > 1000:
            result = math.sqrt(c_cubed) * 10
        else:
            result = math.sqrt(c_cubed) / a

        result += b
        return f"<p style='color: green;'>Result: {result}</p>"

    except ValueError:
        return "<p style='color: red;'>Error: All inputs must be numeric.</p>"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Content-Type: text/html")
        print()
        print("<p style='color: red;'>Error: Three numeric inputs are required.</p>")
    else:
        a = sys.argv[1]
        b = sys.argv[2]
        c = sys.argv[3]
        print("Content-Type: text/html")
        print()
        print("<html><body>")
        print(calculate(a, b, c))
        print("</body></html>")
