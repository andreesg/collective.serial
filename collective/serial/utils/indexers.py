
from plone.indexer.decorator import indexer
from ..serial import ISerial

@indexer(ISerial)
def library_year(object, **kw):
    try:
        if hasattr(object, 'titleAuthorImprintCollation_imprint_year'):
            return object.titleAuthorImprintCollation_imprint_year
        else:
            return ""
    except:
        return ""

@indexer(ISerial)
def serial_priref(object, **kw):
    try:
        if hasattr(object, 'priref'):
            return object.priref
        else:
            return ""
    except:
        return ""

@indexer(ISerial)
def library_author(object, **kw):
    try:
        if hasattr(object, 'titleAuthorImprintCollation_titleAuthor_author'):
            list_authors = []
            items = object.titleAuthorImprintCollation_titleAuthor_author
            if items:
                for item in items:
                    if item['authors']:
                        author = item['authors'][0]
                        if IRelationValue.providedBy(author):
                            author_obj = author.to_object
                            title = getattr(author_obj, 'title', None)
                            if title:
                                list_authors.append(title)
                        else:
                            title = getattr(author, 'title', None)
                            if title:
                                list_authors.append(title)

            return "_".join(list_authors)
        else:
            return ""
    except:
        return ""
        
@indexer(ISerial)
def abstractAndSubjectTerms_subjectTerm_subjectType(object, **kw):
    try:
        if hasattr(object, 'abstractAndSubjectTerms_subjectTerm'):
            terms = []
            items = object.abstractAndSubjectTerms_subjectTerm
            if items:
                for item in items:
                    if item['subjectType']:
                        for term in item['subjectType']:
                            if term:
                                terms.append(term)

            return terms
        else:
            return []
    except:
        return []

@indexer(ISerial)
def abstractAndSubjectTerms_subjectTerm_properName(object, **kw):
    try:
        if hasattr(object, 'abstractAndSubjectTerms_subjectTerm'):
            terms = []
            items = object.abstractAndSubjectTerms_subjectTerm
            if items:
                for item in items:
                    if item['properName']:
                        for term in item['properName']:
                            if term:
                                terms.append(term)

            return terms
        else:
            return []
    except:
        return []

@indexer(ISerial)
def copiesAndShelfMarks_copyDetails_loan(object, **kw):
    try:
        if hasattr(object, 'copiesAndShelfMarks_copyDetails'):
            terms = []
            items = object.copiesAndShelfMarks_copyDetails
            if items:
                for item in items:
                    if item['loanCategory']:
                        for term in item['loanCategory']:
                            if term:
                                terms.append(term)

            return terms
        else:
            return []
    except:
        return []

@indexer(ISerial)
def copiesAndShelfMarks_copyDetails_site(object, **kw):
    try:
        if hasattr(object, 'copiesAndShelfMarks_copyDetails'):
            terms = []
            items = object.copiesAndShelfMarks_copyDetails
            if items:
                for item in items:
                    if item['site']:
                        for term in item['site']:
                            if term:
                                terms.append(term)

            return terms
        else:
            return []
    except:
        return []

@indexer(ISerial)
def abstractAndSubjectTerms_biblForm(object, **kw):
    try:
        if hasattr(object, 'abstractAndSubjectTerms_biblForm'):
            return object.abstractAndSubjectTerms_biblForm
        else:
            return []
    except:
        return []

@indexer(ISerial)
def abstractAndSubjectTerms_materialType(object, **kw):
    try:
        if hasattr(object, 'abstractAndSubjectTerms_materialType'):
            return object.abstractAndSubjectTerms_materialType
        else:
            return []
    except:
        return []

@indexer(ISerial)
def abstractAndSubjectTerms_language(object, **kw):
    try:
        if hasattr(object, 'abstractAndSubjectTerms_language'):
            return object.abstractAndSubjectTerms_language
        else:
            return []
    except:
        return []

@indexer(ISerial)
def abstractAndSubjectTerms_classNumber(object, **kw):
    try:
        if hasattr(object, 'abstractAndSubjectTerms_classNumber'):
            return object.abstractAndSubjectTerms_classNumber
        else:
            return []
    except:
        return []

@indexer(ISerial)
def abstractAndSubjectTerms_geographicalKeyword(object, **kw):
    try:
        if hasattr(object, 'abstractAndSubjectTerms_geographicalKeyword'):
            return object.abstractAndSubjectTerms_geographicalKeyword
        else:
            return []
    except:
        return []



