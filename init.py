# Title: Profanity Filter
# Author Darius 'Alkarion' Strasel
# Todo: pass output in a more meaningful way

import urllib.request
import sys

class ProfanityFilter:
    def __init__(self):
        self.profanities = []
        file_contents = None
        file_args = sys.argv[1:]

        if len(file_args) > 0:
            try:
                with open(file_args[0]) as f:
                    file_contents = f.read()
            except:
                print("Unable to open source document")

            self.process_line(file_contents, 1)
        else:
            self.usage_information()

    def usage_information(self):
        print('Usage: Python init.py "file_argument"')

    def process_line(self, line, batch_size):
        """This function will parse an input string and send values to the profanity checked based on the batched size."""

        new_line = line.split()
        pointer = 1
        index_end = 1
        index_start = 0

        for _ in range(0, len(new_line)):
            if pointer == batch_size:
                result = self.open_connection("%20".join(new_line[index_start:index_end]))
                self.profanities.append(result)
                index_start += pointer
                pointer = 0

            index_end += 1
            pointer += 1

        if index_end - index_start < batch_size:
            self.open_connection("%20".join(new_line[index_start:len(new_line)]))

    def open_connection(self, string_to_check):
        """Open connection to RestAPI and query string input."""
        try:
            connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q={0}".format(string_to_check))
            output = connection.read()

        except:
            print("Unable to connect to URL to check string")
            return

        finally:
            connection.close

        return (output.decode() == "true")

    def count_profanities(self):
        """Count all word instances which are profanities"""
        return self.profanities.count(True)

    def count_non_profanities(self):
        """Count all word instances which are not profanities"""
        return self.profanities.count(False)

p = ProfanityFilter()

print(p.count_profanities())
print(p.count_non_profanities())

#http://isithackday.com/arrpi.php?text=friend

#Could use this link to build a pirate speech translator?