# kepubify
# https://pgaskin.net/kepubify/

# Kepubify converts EPUBs to KEPUBs. Kepubify is fast, lightweight, easy-to-use, and cross platform.
# Features
# Full support of all kepub features
# Extremely fast (about 15x faster and uses 3x less memory than Calibre)
# Batch conversion with full control over the directory structure
# Works from the command line and can be embedded in other applications
# Comprehensive test suite
# Optionally pre-generate covers (can also stretch it to a specific aspect ratio)
# Optionally update Kobo series metadata (even before the book is imported)
# Covergen: Optionally pre-generate covers (can also stretch it to a specific aspect ratio)
# Seriesmeta: Optionally update Kobo series metadata (even before the book is imported)

# Examples
# For the following examples, replace kepubify with the path to the downloaded kepubify.

# To convert a single book by dragging and dropping on Windows:
# Just drag the original epub file over kepubify.exe. The resulting file will be saved to the same directory as the original epub.

# To convert a folder of books by dragging and dropping on Windows:
# Just drag the folder over kepubify.exe. The resulting file will be saved to the same directory as the originals, but with the suffix _converted.

# To convert a single book:
# kepubify /path/to/the/book.epub
# The resulting file will be saved to the current directory.

# To convert a single book with a different output folder:
# kepubify --output "/path/to/save/the/book/" /path/to/the/book.epub
# The resulting file will be saved to specified folder (in this example /path/to/save/the/book/).

# To convert all books in the current folder into a folder called converted:
# kepubify -o "converted" *.epub

# To batch convert a directory of ebooks:
# kepubify /path/to/the/books/
# The converted books will be saved to the original dir with the suffix _converted (e.g. /path/to/the/books_converted).The directory structure of the source is preserved in the output.

# To batch convert a directory of ebooks with a different output folder:
# kepubify -o "/path/to/output/the/converted/books" /path/to/the/books/
# The directory structure of the source is preserved in the output.

# To convert a directory of ebooks, but skipping ones which have already been converted:
# kepubify --update /path/to/the/books/

# To convert a calibre library in-place:
# kepubify --update --inplace --calibre /path/to/calibre/library/

# To convert a folder of books directly on to a Kobo eReader, while simply copying PDF files:
# kepubify --output /path/to/kobo/kepubify --update --copy .pdf /path/to/books/

FROM alpine
LABEL maintainer="sevendollar@gmail.com"

WORKDIR /kobo

RUN apk update && \
        apk add curl && \
        curl -LO https://github.com/pgaskin/kepubify/releases/download/v3.1.6/kepubify-linux-64bit && \
        chmod +x kepubify-linux-64bit && \
        mv kepubify-linux-64bit /usr/bin/kepubify
ENTRYPOINT [ "kepubify" ]