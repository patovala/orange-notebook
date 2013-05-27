#------------------------------------------------------------------------------#
#----                                                                      ----#
#----  Data fixer  for COMP90049 UOM                                       ----#
#----                                                                      ----#
#----  Author: Ivan Patricio Valarezo 601099 @patovala                     ----#
#------------------------------------------------------------------------------#

# fixing the data
import csv


def fixit(filename, trainer=False):
    """Fix the data to get a Orange tab data output, if the trainer is False
    then the ? are not eliminated from the data stream"""
    filedata = filename + ".tab"

    # our expected input is: Sydney,1859,03,28,0.0,23.6,14.3,Mon

    #[station] The name of the station
    #[year] The year in which the observation(s) took place
    #[month] The month in which the observation(s) took place
    #[day] The day of the month on which the observation(s) took place
    #[precipitation] The aggregated precipitation observed (in mm)
    #[min\_temp] The minimum observed temperature (in degrees Celsius)
    #[max\_temp] The maximum observed temperature (in degrees Celsius)
    #[avg\_temp] The average of the observed temperature readings
    #           (in degrees Celsius); if only one reading took place for a
    #           given day, this will be the same as the minimum and maximum
    #           temperature
    #[max\_wind] The maximum recorded wind reading (in metres per second)
    #[min\_wind] The minimum observed sky ceiling (in metres)
    #[max\_sky] The maximum observed sky ceiling (in metres)
    #[avg\_sky] The average of the observed sky ceiling readings (in metres)
    #[min\_vis] The minimum observed visibility (in metres)
    #[max\_vis] The maximum observed visibility (in metres)
    #[avg\_vis] The average of the observed visibility readings (in metres)
    #[min\_dew] The minimum observed dew point (in degrees Celsius)
    #[max\_dew] The maximum observed dew point (in degrees Celsius)
    #[avg\_dew] The average of the observed dew point readings (in degrees
    #           Celsius)
    #[min\_pres] The minimum observed barometric pressure, normalised to sea
    #           level (in hectopascals)
    #[max\_pres] The maximum observed barometric pressure (in hectopascals)
    #[avg\_pres] The average of the observed pressure readings (in hectopascals)
    #[weekday] The day of the week

    features = ["station", "year", "month", "day", "precipitation", "min_temp",
                "max_temp", "avg_temp", "max_wind", "min_wind", "max_sky",
                "avg_sky", "min_vis", "max_vis", "avg_vis", "min_dew",
                "max_dew", "avg_dew", "min_pres", "max_pres", "avg_pres",
                "weekday"]

    #features2 = ["string", "c", "c", "c", "d", "d", "d", "d", "d", "d", "d",
    # PV with an string at the begining the data screws really bad
    features2 = ["d", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c",
                "c",  "c",  "c",  "c",  "c", "c", "c",  "c",  "c",  "c",  "d"]

    features3 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                "", "", "", "", "", "", "class"]

    csv.register_dialect('tabs', delimiter='\t')

    with open(filename) as f:
        reader = csv.reader(f)
        with open(filedata, "w") as fd:
            writer = csv.writer(fd, dialect='tabs')
            writer.writerow(features)
            writer.writerow(features2)
            writer.writerow(features3)
            for row in reader:
                if trainer and not u'?' in row:
                    writer.writerow(row)
                if not trainer:
                    writer.writerow(row)

    print "done %s (%s,%s,%s)" % (filedata, len(features), len(features2), len(features3))
