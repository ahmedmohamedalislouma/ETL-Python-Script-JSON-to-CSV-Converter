# ETL-Python-Script-JSON-to-CSV-Converter
# US government URL Data Converter

This Python script converts JSON files containing US government URL data into separate CSV files, each representing a single JSON file. The script transforms the JSON data into a structured DataFrame and applies various data manipulations to generate the desired CSV output. The resulting CSV files contain information about web browsers, operating systems, URLs, cities, geographic coordinates, time zones, and timestamps.

## Problem Description

In 2012, the URL shortening service Bitly partnered with the US government website USA.gov to gather anonymous data from users who shortened .gov or .mil links. The provided JSON files contain important keys related to the web browsing activity, such as web browser and operating system information, time zone, referring URL, target URL, timestamps, city, and geographic coordinates.

## Requirements

- Python 3.x
- Pandas library

## Usage

1. Navigate to the project directory:

   ```
   cd us-url-data-converter
   ```

2. Run the script with the following command:

   ```
   python convert_json_to_csv.py <directory_path> [-u]
   ```

   - `<directory_path>`: Path to the directory containing the JSON files to be converted.
   - `-u` or `--unix`: (Optional) Maintain UNIX formatting for timestamps.

3. After execution, the script will generate separate CSV files for each JSON file in the specified directory.

## Output

The generated CSV files will have the following columns:

- `web_browser`: The web browser used to request the service.
- `operating_sys`: The operating system that initiated the request.
- `from_url`: The main URL from which the user originated.
- `to_url`: The shortened URL to which the user navigated.
- `city`: The city from which the request was sent.
- `longitude`: The longitude of the request location.
- `latitude`: The latitude of the request location.
- `time_zone`: The time zone associated with the city.
- `time_in`: The timestamp when the request started.
- `time_out`: The timestamp when the request ended.


## Notes

- Incomplete instances in the JSON files may result in NaN values in the transformations. The script ensures that the final DataFrames have no NaN values.

## Example

Suppose we have a directory called `json_files` that contains multiple JSON files. To convert them to CSV, run the following command:

```
python convert_json_to_csv.py json_files -u
```

This command will convert the JSON files to CSV format using UNIX formatting for timestamps. The resulting CSV files will be saved in the same directory as the JSON files.

## Output Summary

After the processing is completed for each JSON file, the script will print the following information in the terminal:

```
Number of rows: <count_row> rows   File Path: <a>
Execution time: <elapsed_time> seconds
```

- `<count_row>`: The number of rows in the transformed DataFrame.
- `<a>`: The file path of the generated CSV file.
- `<elapsed_time>`: The execution time of the script in seconds.

Please ensure that the required Python version and the Pandas library are installed before running the script.
