import json
import os


def json_to_csv(dir_path="./Convert Json to Csv", filename="input.json"):
    try:
        # Build input path
        input_path = os.path.join(dir_path, filename)

        # Read JSON
        with open(input_path, "r") as f:
            data = json.loads(f.read())

        # Build CSV content
        output = ",".join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'

        # Build output path (same folder)
        output_path = os.path.join(dir_path, "output.csv")

        # Write CSV in Convert Json to Csv folder
        with open(output_path, "w") as f:
            f.write(output)

        print(f"CSV written to: {output_path}")

    except Exception as ex:
        print(f"Error: {str(ex)}")


if __name__ == "__main__":
    json_to_csv()
