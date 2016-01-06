#-*- coding:utf-8 -*-

class Item(object):

    """
    Intermediary object between bibtex/zotero and unite source output.
    """

    def combine(self):
        self.combined = u"\n[{}]\nKey: {}\nTitle: {}\nAuthor(s): {}\nDate: {}\nTags:{}\nAbstract: {}\nJournal: {}\nIssue: {}\nVolume: {}\nPages: {}\nPublisher: {}\nLang: {}\nFile(s): {}\nURL:{}\nDOI:{}\nISBN:{}\nAnnotation: {}".format(
            self.type,
            self.key,
            self.title,
            self.author, 
            self.date,
            self.tags,
            self.abstract,
            self.journal, 
            self.issue, 
            self.volume, 
            self.pages, 
            self.publisher, 
            self.language, 
            self.file, 
            self.url, 
            self.doi, 
            self.isbn, 
            self.notes)

    def describe(self, source_field, desc_fields, desc_format):
        # Get strings for description fields.
        desc_strings = []
        for desc_field in desc_fields:
            try:
                getattr(self, desc_field)
            except AttributeError:
                return 'Error at "{}" field of g:unite_bibtex_description_fields. Check your vimrc.'.format(desc_field)

            desc_strings.append(getattr(self, desc_field))

        # Insert the source field if not present in the description,
        # and put brackets around it wherever it is.
        source_string = ""
        if source_field in desc_fields:
            source_index = desc_fields.index(source_field)
            desc_strings[source_index] = "【{}】".format(desc_strings[source_index]) 
        else:
            if not source_field in ["combined","file"]:
                source_string = " 【{}】".format(getattr(self, source_field))

        return desc_format.format(*desc_strings) + source_string
