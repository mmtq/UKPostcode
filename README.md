# UK Postcode Finder

A Django web application that provides comprehensive information on every UK postcode across England, Scotland, Wales, and Northern Ireland. Browse by region, county, district, or ward, or search directly by postcode.

**Live site:** https://findpostcode.uk

---

## Features

- **Full UK coverage** – England, Scotland, Wales, and Northern Ireland.
- **Rich postcode data** – latitude/longitude, easting/northing, OS grid reference, altitude, distance to sea, and more.
- **Administrative boundaries** – regions, counties, districts, wards, constituencies (including 2024 boundaries), parishes, LSOA/MSOA codes, and IMD data.
- **Local amenities** – nearby schools and bus stops (powered by the Doogal API).
- **Hierarchical browsing** – drill down from country → region → county → district → ward → individual postcode.
- **Postcode & area search** – search by postcode string or by area name across all four nations.
- **JSON API endpoint** – fetch raw postcode data programmatically.
- **Blog** – articles explaining the UK postcode format.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 5.0.6 |
| Database | SQLite (default) |
| Frontend | HTML templates with Tailwind CSS |
| External data | [Doogal](https://www.doogal.co.uk/) postcode API |

---

## Project Structure

```
UKPostcode/          # Django project settings, root URLs, and shared views
England/             # England app – regions, counties, districts, wards, postcodes
Scotland/            # Scotland app – districts, wards, postcodes
wales/               # Wales app – districts, wards, postcodes
NorthernIreland/     # Northern Ireland app – districts, wards, postcodes
templates/           # Shared HTML templates
static/              # Static assets (CSS, images, JS)
manage.py
importdb.py          # Utility script for bulk-importing postcode CSV data
```

---

## Prerequisites

- Python 3.10+
- pip

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/mmtq/UKPostcode.git
   cd UKPostcode
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install django requests
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   The site will be available at http://127.0.0.1:8000/.

> **Note:** The database ships empty. To populate it with real postcode data, obtain CSV files from a source such as [Doogal](https://www.doogal.co.uk/PostcodeDownloads) or the [ONS Postcode Directory](https://geoportal.statistics.gov.uk/) and use `importdb.py` as a reference for bulk-importing records into each nation's `PostcodeData` model.

---

## URL Structure

| URL | Description |
|---|---|
| `/` | Home page |
| `/search/?s=<term>` | Search postcodes or areas |
| `/england/` | Browse England by region |
| `/england/<region>/` | Counties in a region |
| `/england/<region>/<county>/` | Districts in a county |
| `/england/<region>/<county>/<district>/` | Wards in a district |
| `/england/<region>/<county>/<district>/<ward>/` | Postcodes in a ward |
| `/england/<POSTCODE>/` | Individual England postcode detail |
| `/scotland/` | Browse Scotland by district |
| `/scotland/<district>/` | Wards in a district |
| `/scotland/<district>/<ward>/` | Postcodes in a ward |
| `/scotland/<POSTCODE>/` | Individual Scotland postcode detail |
| `/wales/` | Browse Wales |
| `/nir/` | Browse Northern Ireland |
| `/area/<prefix>/` | All postcodes starting with a prefix |
| `/district/<prefix>/` | All postcodes in a district prefix |
| `/nearby-schools/` | Find schools near a postcode |
| `/nearby-bus-stops/` | Find bus stops near a postcode |
| `/api/fetch-data/?search=<postcode>` | JSON postcode data |
| `/blog/uk-postcode-format/` | Blog: UK postcode format guide |
| `/about-us/` | About page |
| `/contact-us/` | Contact page |
| `/privacy-policy/` | Privacy policy |
| `/sitemap.xml` | XML sitemap |

---

## API

**Endpoint:** `GET /api/fetch-data/?search=<postcode>`

Returns a JSON object with detailed information for the given postcode, sourced from the Doogal API.

**Example:**

```
GET /api/fetch-data/?search=SW1A1AA
```

---

## Postcode Data Fields

Each postcode record stores the following information:

| Field | Description |
|---|---|
| `postcode` | Formatted postcode |
| `latitude` / `longitude` | WGS84 coordinates |
| `easting` / `northing` | OS National Grid coordinates |
| `grid_ref` | OS grid reference |
| `altitude` | Altitude in metres |
| `distance_to_sea` | Distance to coastline |
| `region` | Administrative region |
| `county` / `county_code` | County name and ONS code |
| `district` / `district_code` | District name and ONS code |
| `ward` / `ward_code` | Ward name and ONS code |
| `constituency` / `constituency_code` | Westminster constituency |
| `constituency_name_2024` / `constituency_code_2024` | 2024 boundary constituency |
| `parish` / `parish_code` | Civil parish |
| `local_authority` | Local authority name |
| `police_force` | Policing area |
| `water_company` / `sewage_company` | Utility providers |
| `population` / `households` | Census statistics |
| `lsoa_code` / `lower_layer_super_output_area` | 2011 LSOA |
| `lsoa21_code` / `lower_layer_super_output_area_2021` | 2021 LSOA |
| `msoa_code` / `middle_layer_super_output_area` | 2011 MSOA |
| `msoa21_code` / `middle_layer_super_output_area_2021` | 2021 MSOA |
| `index_of_multiple_deprivation` / `imd_decile` | Deprivation index |
| `rural_urban` | Rural/urban classification |
| `built_up_area` / `built_up_subdivision` | Built-up area name |
| `nearest_station` / `distance_to_station` | Nearest railway station |
| `postcode_area` / `postcode_district` | Postcode area and district prefix |
| `plus_code` | Google Plus Code |
| `itl_level_2` / `itl_level_3` | International Territorial Level codes |

---

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file included in the repository.
