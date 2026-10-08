import pandas as pd
import numpy as np


# Crop data using a list of dictionaries
crop_data = [
    {
        "crop": "Rice",
        "soil": "Clay",
        "water": "High",
        "min_temp": 20,
        "max_temp": 35
    },
    {
        "crop": "Wheat",
        "soil": "Loamy",
        "water": "Medium",
        "min_temp": 15,
        "max_temp": 25
    },
    {
        "crop": "Maize",
        "soil": "Loamy",
        "water": "Medium",
        "min_temp": 18,
        "max_temp": 30
    },
    {
        "crop": "Groundnut",
        "soil": "Sandy",
        "water": "Low",
        "min_temp": 20,
        "max_temp": 30
    },
    {
        "crop": "Cotton",
        "soil": "Black",
        "water": "Medium",
        "min_temp": 21,
        "max_temp": 35
    },
    {
        "crop": "Sugarcane",
        "soil": "Loamy",
        "water": "High",
        "min_temp": 20,
        "max_temp": 35
    }
]


# Tuples for fixed options
soil_types = ("Clay", "Loamy", "Sandy", "Black")
water_levels = ("Low", "Medium", "High")


# Convert crop data into a Pandas DataFrame
df = pd.DataFrame(crop_data)


# NumPy calculation
average_temperature = np.mean(
    (df["min_temp"] + df["max_temp"]) / 2
)

print(
    "Average ideal temperature:",
    round(average_temperature, 2)
)


# List comprehension
medium_water_crops = [
    crop["crop"]
    for crop in crop_data
    if crop["water"] == "Medium"
]

print(
    "Medium water crops:",
    medium_water_crops
)


# Function to calculate temperature suitability
def temperature_score(
    user_temperature,
    min_temperature,
    max_temperature
):

    ideal_temperature = (
        min_temperature + max_temperature
    ) / 2

    temperature_range = (
        max_temperature - min_temperature
    )

    difference = abs(
        user_temperature - ideal_temperature
    )

    if difference >= temperature_range:
        return 0

    score = 1 - (
        difference / temperature_range
    )

    return score


# Function to calculate total crop suitability
def calculate_suitability(
    crop,
    user_temperature,
    user_soil,
    user_water
):

    temp_score = temperature_score(
        user_temperature,
        crop["min_temp"],
        crop["max_temp"]
    )

    if crop["soil"] == user_soil:
        soil_score = 1
    else:
        soil_score = 0

    if crop["water"] == user_water:
        water_score = 1
    else:
        water_score = 0

    scores = np.array([
        temp_score,
        soil_score,
        water_score
    ])

    final_score = np.mean(scores) * 100

    return round(final_score, 2)


# Function to create interactive crop cards
def make_crop_card(crop):

    if crop["water"] == "High":
        water_text = "High Water"

    elif crop["water"] == "Medium":
        water_text = "Medium Water"

    else:
        water_text = "Low Water"

    return f"""
    <div
        class="crop-card"
        onclick="selectCrop(this)"
    >

        <div class="card-top">

            <div class="crop-icon">
                🌱
            </div>

            <span class="water-badge">
                💧 {water_text}
            </span>

        </div>


        <h3>{crop["crop"]}</h3>

        <p class="crop-description">
            Suitable for {crop["soil"]} soil
        </p>


        <div class="card-line"></div>


        <div class="crop-basic-info">

            <div>
                <span>🌍</span>
                <small>Soil</small>
                <strong>{crop["soil"]}</strong>
            </div>

            <div>
                <span>🌡️</span>
                <small>Temperature</small>
                <strong>
                    {crop["min_temp"]}°C -
                    {crop["max_temp"]}°C
                </strong>
            </div>

        </div>


        <div class="card-details">

            <p>
                <b>Water Requirement:</b>
                {water_text}
            </p>

            <p>
                <b>Ideal Temperature:</b>
                {crop["min_temp"]}°C -
                {crop["max_temp"]}°C
            </p>

            <div class="suitability-label">
                Suitable Conditions
            </div>

            <div class="progress-background">

                <div class="progress-bar">
                </div>

            </div>

        </div>


        <div class="click-message">
            Click to explore
        </div>

    </div>
    """


# Generate crop cards using a loop
crop_cards = ""

for crop in crop_data:
    crop_cards += make_crop_card(crop)


# Generate JavaScript crop data
javascript_crop_data = "["

for crop in crop_data:

    javascript_crop_data += f"""
    {{
        crop: "{crop["crop"]}",
        soil: "{crop["soil"]}",
        water: "{crop["water"]}",
        minTemp: {crop["min_temp"]},
        maxTemp: {crop["max_temp"]}
    }},
    """

javascript_crop_data += "]"


# Generate HTML using Python f-string
html_content = f"""
<!DOCTYPE html>

<html>

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>AI in Agriculture</title>


    <style>

        * {{
            box-sizing: border-box;
        }}


        body {{

            font-family: Arial, sans-serif;

            margin: 0;

            background:
                linear-gradient(
                    135deg,
                    #eef8ef,
                    #f8fff9
                );

            color: #1f3d2b;

        }}


        /* Header */

        header {{

            background:
                linear-gradient(
                    135deg,
                    #1b5e20,
                    #43a047
                );

            color: white;

            text-align: center;

            padding: 55px 20px;

            position: relative;

            overflow: hidden;

        }}


        header::before {{

            content: "🌿";

            position: absolute;

            font-size: 130px;

            opacity: 0.08;

            left: 8%;

            top: -25px;

            animation: floatLeaf 4s ease-in-out infinite;

        }}


        header::after {{

            content: "🌱";

            position: absolute;

            font-size: 100px;

            opacity: 0.08;

            right: 8%;

            bottom: -20px;

            animation: floatLeaf 5s ease-in-out infinite;

        }}


        header h1 {{

            margin: 0;

            font-size: 42px;

            position: relative;

            z-index: 1;

            animation: titleAppear 1s ease;

        }}


        header p {{

            font-size: 18px;

            margin-top: 12px;

            position: relative;

            z-index: 1;

            opacity: 0.95;

        }}


        /* Introduction */

        .intro {{

            text-align: center;

            padding: 35px 20px;

            max-width: 900px;

            margin: auto;

            animation: fadeUp 0.9s ease;

        }}


        .intro h2 {{

            color: #2e7d32;

            font-size: 28px;

        }}


        .intro p {{

            line-height: 1.7;

            color: #4c6252;

        }}


        /* Main container */

        .container {{

            width: 90%;

            max-width: 1100px;

            margin: auto;

        }}


        /* Input section */

        .input-section {{

            background: white;

            padding: 30px;

            margin: 25px 0 45px;

            border-radius: 20px;

            box-shadow:
                0 8px 25px
                rgba(46, 125, 50, 0.12);

            border: 1px solid #dcefe0;

        }}


        .input-section h2 {{

            text-align: center;

            color: #2e7d32;

            margin-bottom: 25px;

        }}


        label {{

            display: block;

            margin-top: 16px;

            font-weight: bold;

        }}


        input,
        select {{

            width: 100%;

            padding: 13px;

            margin-top: 7px;

            border: 1px solid #b7c8ba;

            border-radius: 9px;

            font-size: 15px;

            background: #fbfffc;

            transition:
                border 0.3s ease,
                box-shadow 0.3s ease;

        }}


        input:focus,
        select:focus {{

            outline: none;

            border-color: #43a047;

            box-shadow:
                0 0 0 3px
                rgba(67, 160, 71, 0.15);

        }}


        button {{

            width: 100%;

            padding: 14px;

            margin-top: 22px;

            background:
                linear-gradient(
                    135deg,
                    #2e7d32,
                    #43a047
                );

            color: white;

            border: none;

            border-radius: 9px;

            font-size: 16px;

            font-weight: bold;

            cursor: pointer;

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease;

        }}


        button:hover {{

            transform: translateY(-3px);

            box-shadow:
                0 8px 18px
                rgba(46, 125, 50, 0.3);

        }}


        button:active {{

            transform: scale(0.98);

        }}


        /* Result */

        #result {{

            margin-top: 25px;

            padding: 25px;

            background:
                linear-gradient(
                    135deg,
                    #e8f5e9,
                    #f4fff5
                );

            border-left: 5px solid #2e7d32;

            border-radius: 12px;

            display: none;

            animation: resultAppear 0.5s ease;

        }}


        /* Crop section */

        .crop-heading {{

            text-align: center;

            margin-bottom: 25px;

        }}


        .crop-heading h2 {{

            color: #2e7d32;

        }}


        .crop-heading p {{

            color: #607064;

        }}


        /* Crop grid */

        .crop-grid {{

            display: grid;

            grid-template-columns:
                repeat(
                    auto-fit,
                    minmax(260px, 1fr)
                );

            gap: 25px;

            margin-bottom: 50px;

        }}


        /* Interactive crop card */

        .crop-card {{

            background: rgba(255, 255, 255, 0.95);

            padding: 24px;

            border-radius: 20px;

            border: 1px solid #dcefe0;

            box-shadow:
                0 6px 16px
                rgba(0, 0, 0, 0.08);

            cursor: pointer;

            position: relative;

            overflow: hidden;

            transform: translateY(25px);

            opacity: 0;

            animation:
                cardAppear 0.7s ease forwards;

            transition:
                transform 0.35s ease,
                box-shadow 0.35s ease,
                border-color 0.35s ease,
                background 0.35s ease;

        }}


        .crop-card:nth-child(1) {{
            animation-delay: 0.1s;
        }}

        .crop-card:nth-child(2) {{
            animation-delay: 0.2s;
        }}

        .crop-card:nth-child(3) {{
            animation-delay: 0.3s;
        }}

        .crop-card:nth-child(4) {{
            animation-delay: 0.4s;
        }}

        .crop-card:nth-child(5) {{
            animation-delay: 0.5s;
        }}

        .crop-card:nth-child(6) {{
            animation-delay: 0.6s;
        }}


        .crop-card::before {{

            content: "";

            position: absolute;

            width: 100px;

            height: 100px;

            background: #e8f5e9;

            border-radius: 50%;

            right: -40px;

            top: -40px;

            transition:
                transform 0.4s ease;

        }}


        .crop-card:hover::before {{

            transform: scale(2.2);

        }}


        .crop-card:hover {{

            transform:
                translateY(-10px)
                rotateX(2deg);

            box-shadow:
                0 15px 30px
                rgba(46, 125, 50, 0.18);

            border-color: #81c784;

        }}


        .crop-card.active {{

            transform:
                translateY(-8px)
                scale(1.03);

            border-color: #43a047;

            background: #f6fff7;

            box-shadow:
                0 18px 35px
                rgba(46, 125, 50, 0.22);

        }}


        .card-top {{

            display: flex;

            align-items: center;

            justify-content: space-between;

            position: relative;

            z-index: 2;

        }}


        .crop-icon {{

            width: 58px;

            height: 58px;

            display: flex;

            align-items: center;

            justify-content: center;

            background: #e8f5e9;

            border-radius: 50%;

            font-size: 30px;

            transition:
                transform 0.4s ease;

        }}


        .crop-card:hover .crop-icon {{

            transform:
                rotate(-8deg)
                scale(1.15);

        }}


        .water-badge {{

            background: #e3f2fd;

            color: #1565c0;

            padding: 7px 10px;

            border-radius: 20px;

            font-size: 12px;

            font-weight: bold;

        }}


        .crop-card h3 {{

            color: #2e7d32;

            font-size: 25px;

            margin: 20px 0 7px;

            position: relative;

            z-index: 2;

        }}


        .crop-description {{

            color: #66766a;

            position: relative;

            z-index: 2;

        }}


        .card-line {{

            height: 1px;

            background: #e0ebe2;

            margin: 18px 0;

        }}


        .crop-basic-info {{

            display: grid;

            grid-template-columns: 1fr 1fr;

            gap: 10px;

        }}


        .crop-basic-info div {{

            background: #f4f8f4;

            padding: 12px;

            border-radius: 10px;

            display: flex;

            flex-direction: column;

            gap: 4px;

        }}


        .crop-basic-info span {{

            font-size: 20px;

        }}


        .crop-basic-info small {{

            color: #718074;

        }}


        .crop-basic-info strong {{

            color: #294d32;

            font-size: 13px;

        }}


        /* Hidden details */

        .card-details {{

            max-height: 0;

            opacity: 0;

            overflow: hidden;

            transform: translateY(-10px);

            transition:
                max-height 0.5s ease,
                opacity 0.4s ease,
                transform 0.4s ease;

        }}


        .crop-card.active .card-details {{

            max-height: 300px;

            opacity: 1;

            transform: translateY(0);

            margin-top: 18px;

        }}


        .suitability-label {{

            font-size: 13px;

            font-weight: bold;

            margin-top: 15px;

            margin-bottom: 7px;

            color: #2e7d32;

        }}


        .progress-background {{

            height: 9px;

            background: #dcebdd;

            border-radius: 20px;

            overflow: hidden;

        }}


        .progress-bar {{

            height: 100%;

            width: 80%;

            background:
                linear-gradient(
                    90deg,
                    #43a047,
                    #81c784
                );

            border-radius: 20px;

            transform: scaleX(0);

            transform-origin: left;

            transition:
                transform 0.8s ease;

        }}


        .crop-card.active .progress-bar {{

            transform: scaleX(1);

        }}


        .click-message {{

            text-align: center;

            color: #43a047;

            font-size: 12px;

            font-weight: bold;

            margin-top: 18px;

            transition:
                opacity 0.3s ease;

        }}


        .crop-card.active .click-message {{

            opacity: 0.7;

        }}


        /* AI help section */

        .help-section {{

            background: white;

            padding: 30px;

            margin: 35px 0;

            border-radius: 20px;

            box-shadow:
                0 6px 18px
                rgba(0, 0, 0, 0.07);

        }}


        .help-section h2 {{

            color: #2e7d32;

        }}


        .help-section li {{

            margin: 14px 0;

            line-height: 1.6;

        }}


        /* Footer */

        footer {{

            background:
                linear-gradient(
                    135deg,
                    #1b5e20,
                    #2e7d32
                );

            color: white;

            text-align: center;

            padding: 20px;

            margin-top: 50px;

        }}


        /* Animations */

        @keyframes cardAppear {{

            from {{
                opacity: 0;
                transform:
                    translateY(30px)
                    scale(0.95);
            }}

            to {{
                opacity: 1;
                transform:
                    translateY(0)
                    scale(1);
            }}

        }}


        @keyframes titleAppear {{

            from {{
                opacity: 0;
                transform: translateY(-20px);
            }}

            to {{
                opacity: 1;
                transform: translateY(0);
            }}

        }}


        @keyframes fadeUp {{

            from {{
                opacity: 0;
                transform: translateY(20px);
            }}

            to {{
                opacity: 1;
                transform: translateY(0);
            }}

        }}


        @keyframes resultAppear {{

            from {{
                opacity: 0;
                transform: scale(0.96);
            }}

            to {{
                opacity: 1;
                transform: scale(1);
            }}

        }}


        @keyframes floatLeaf {{

            0%, 100% {{
                transform: translateY(0);
            }}

            50% {{
                transform: translateY(-15px);
            }}

        }}


        /* Mobile */

        @media (max-width: 600px) {{

            header h1 {{
                font-size: 32px;
            }}

            .crop-grid {{
                grid-template-columns: 1fr;
            }}

            .crop-basic-info {{
                grid-template-columns: 1fr;
            }}

        }}

    </style>

</head>


<body>


    <header>

        <h1>AI in Agriculture</h1>

        <p>
            Smart Crop Recommendation System
        </p>

    </header>


    <section class="intro">

        <h2>How AI Helps Agriculture</h2>

        <p>
            Artificial Intelligence can help farmers
            make better decisions by analysing soil,
            temperature and water availability.
        </p>

        <p>
            This project demonstrates a simple
            AI-inspired crop recommendation system
            using Python.
        </p>

    </section>


    <div class="container">


        <!-- Recommendation section -->

        <section class="input-section">

            <h2>
                🌾 Find the Best Crop
            </h2>


            <label for="temperature">
                Temperature (°C)
            </label>

            <input
                type="number"
                id="temperature"
                placeholder="Example: 28"
            >


            <label for="soil">
                Soil Type
            </label>

            <select id="soil">

                <option value="Clay">
                    Clay
                </option>

                <option value="Loamy">
                    Loamy
                </option>

                <option value="Sandy">
                    Sandy
                </option>

                <option value="Black">
                    Black
                </option>

            </select>


            <label for="water">
                Water Availability
            </label>

            <select id="water">

                <option value="High">
                    High
                </option>

                <option value="Medium">
                    Medium
                </option>

                <option value="Low">
                    Low
                </option>

            </select>


            <button onclick="recommendCrop()">

                🌱 Get Crop Recommendation

            </button>


            <div id="result"></div>

        </section>


        <!-- Crop cards -->

        <section>

            <div class="crop-heading">

                <h2>
                    🌿 Explore Crops
                </h2>

                <p>
                    Click on a crop card to explore
                    more information.
                </p>

            </div>


            <div class="crop-grid">

                {crop_cards}

            </div>

        </section>


        <!-- How AI helps -->

        <section class="help-section">

            <h2>
                🤖 How AI Helps in Agriculture
            </h2>

            <ul>

                <li>
                    AI can analyse soil and environmental
                    conditions to recommend suitable crops.
                </li>

                <li>
                    AI can process large amounts of
                    agricultural data faster than manual
                    analysis.
                </li>

                <li>
                    AI-based systems can support farmers
                    in making better farming decisions.
                </li>

            </ul>

        </section>


    </div>


    <footer>

        AI in Agriculture | Crop Recommendation System

    </footer>


    <script>


        const crops = {javascript_crop_data};


        // Function for interactive crop cards
        function selectCrop(card) {{

            const cards =
                document.querySelectorAll(
                    ".crop-card"
                );


            cards.forEach(function(item) {{

                if (item !== card) {{

                    item.classList.remove(
                        "active"
                    );

                }}

            }});


            card.classList.toggle("active");

        }}


        // Function for temperature score
        function getTemperatureScore(
            userTemperature,
            minTemperature,
            maxTemperature
        ) {{

            const idealTemperature =
                (minTemperature + maxTemperature)
                / 2;


            const temperatureRange =
                maxTemperature - minTemperature;


            const difference =
                Math.abs(
                    userTemperature -
                    idealTemperature
                );


            if (
                difference >= temperatureRange
            ) {{

                return 0;

            }}


            return 1 -
                (
                    difference /
                    temperatureRange
                );

        }}


        // Function for crop suitability
        function calculateSuitability(
            crop,
            temperature,
            soil,
            water
        ) {{

            const tempScore =
                getTemperatureScore(
                    temperature,
                    crop.minTemp,
                    crop.maxTemp
                );


            const soilScore =
                crop.soil === soil
                ? 1
                : 0;


            const waterScore =
                crop.water === water
                ? 1
                : 0;


            const finalScore =
                (
                    tempScore +
                    soilScore +
                    waterScore
                ) / 3 * 100;


            return finalScore;

        }}


        // Function for crop recommendation
        function recommendCrop() {{

            const temperature =
                parseFloat(
                    document.getElementById(
                        "temperature"
                    ).value
                );


            const soil =
                document.getElementById(
                    "soil"
                ).value;


            const water =
                document.getElementById(
                    "water"
                ).value;


            const result =
                document.getElementById(
                    "result"
                );


            if (isNaN(temperature)) {{

                result.style.display =
                    "block";


                result.innerHTML =
                    "<b>Please enter a valid temperature.</b>";


                return;

            }}


            let results = [];


            for (let crop of crops) {{

                const score =
                    calculateSuitability(
                        crop,
                        temperature,
                        soil,
                        water
                    );


                results.push({{

                    crop: crop.crop,

                    score: score

                }});

            }}


            results.sort(
                (a, b) =>
                    b.score - a.score
            );


            const bestCrop =
                results[0];


            let output = `

                <h2>
                    🌱 Recommended Crop:
                    ${{bestCrop.crop}}
                </h2>

                <h3>
                    Suitability Score:
                    ${{bestCrop.score.toFixed(2)}}%
                </h3>

                <p>
                    <b>Top Recommendations:</b>
                </p>

                <ol>

            `;


            for (
                let item of results.slice(0, 3)
            ) {{

                output += `

                    <li>
                        ${{item.crop}} -
                        ${{item.score.toFixed(2)}}%
                    </li>

                `;

            }}


            output += "</ol>";


            result.innerHTML =
                output;


            result.style.display =
                "block";

        }}

    </script>


</body>

</html>
"""


# Save the generated HTML file
with open("index.html", "w") as file:

    file.write(html_content)


print()

print(
    "AI in Agriculture webpage generated successfully!"
)

print(
    "Open index.html in your browser."
)
