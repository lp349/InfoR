from bs4 import BeautifulSoup
import os

class ExtractFromHTML:
    """
    Implements a script to extract information from HTML documents.
    The script can either extract plaintext or hyperlinks from the
    HTML documents
    """
    def __init__(self, directory):
        """
        Arguments:
            directory - Directory of HTML documents to be searched.
        """
        self.corpus = os.listdir(directory)
        self.soup = {}
        for filename in self.corpus:
            f = os.path.join(directory, filename)
            with open(f) as doc:
                info = doc.read()
                soup = BeautifulSoup(info)
                self.soup[filename] = soup

    def write_plaintext(self, out_directory):
        """
        Writes the plaintext components of all the HTML docs.

        Arguments:
            out_directory : the output directory for the text files.
        """
        for filename, soup in self.soup.iteritems():
            outfile = os.path.splitext(filename)[0]
            outfile = os.path.join(out_directory, outfile + ".txt")
            with open(outfile, 'w') as out:
                out.write(soup.get_text().encode('utf8'))

if __name__ == "__main__":
    extract = ExtractFromHTML('Examples/HTML_Data/')
    extract.write_plaintext('Examples/Out_Data/')
