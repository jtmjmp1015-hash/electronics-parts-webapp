from flask import Flask, render_template, request, abort

app = Flask(__name__)

PARTS = [
    {
        "id": 1,
        "name": "Carbon Film Resistor 1kΩ",
        "category": "Resistor",
        "price": 10,
        "stock": 120,
        "description": "A general-purpose resistor used in many basic circuits."
    },
    {
        "id": 2,
        "name": "Metal Film Resistor 10kΩ",
        "category": "Resistor",
        "price": 15,
        "stock": 95,
        "description": "A precise resistor with stable characteristics."
    },
    {
        "id": 3,
        "name": "Ceramic Capacitor 100nF",
        "category": "Capacitor",
        "price": 20,
        "stock": 200,
        "description": "A small capacitor often used for noise reduction and decoupling."
    },
    {
        "id": 4,
        "name": "Electrolytic Capacitor 100uF",
        "category": "Capacitor",
        "price": 30,
        "stock": 80,
        "description": "A polarized capacitor often used in power supply circuits."
    },
    {
        "id": 5,
        "name": "Red LED 5mm",
        "category": "LED",
        "price": 25,
        "stock": 150,
        "description": "A standard red LED for indicator lights and simple projects."
    },
    {
        "id": 6,
        "name": "Blue LED 5mm",
        "category": "LED",
        "price": 25,
        "stock": 140,
        "description": "A bright blue LED for decorative and indicator use."
    },
    {
        "id": 7,
        "name": "NPN Transistor 2N2222",
        "category": "Transistor",
        "price": 40,
        "stock": 60,
        "description": "A common transistor used for switching and amplification."
    },
    {
        "id": 8,
        "name": "MOSFET IRF520",
        "category": "Transistor",
        "price": 80,
        "stock": 35,
        "description": "A MOSFET suitable for controlling motors and higher loads."
    },
    {
        "id": 9,
        "name": "Photoresistor Sensor",
        "category": "Sensor",
        "price": 60,
        "stock": 50,
        "description": "A light-sensitive component used to detect brightness."
    },
    {
        "id": 10,
        "name": "Temperature Sensor LM35",
        "category": "Sensor",
        "price": 120,
        "stock": 20,
        "description": "An analog temperature sensor for measurement projects."
    }
]

@app.route("/")
def index():
    keyword = request.args.get("keyword", "").strip()
    category = request.args.get("category", "").strip()

    filtered = PARTS

    if keyword:
        filtered = [
            part for part in filtered
            if keyword.lower() in part["name"].lower()
            or keyword.lower() in part["description"].lower()
        ]

    if category:
        filtered = [
            part for part in filtered
            if part["category"] == category
        ]

    categories = sorted(set(part["category"] for part in PARTS))

    return render_template(
        "index.html",
        parts=filtered,
        keyword=keyword,
        selected_category=category,
        categories=categories
    )

@app.route("/part/<int:part_id>")
def part_detail(part_id):
    part = next((p for p in PARTS if p["id"] == part_id), None)

    if part is None:
        abort(404)

    return render_template("detail.html", part=part)

if __name__ == "__main__":
    app.run(debug=True)