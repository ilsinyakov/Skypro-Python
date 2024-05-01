from string_utils import StringUtils

import pytest


@pytest.mark.parametrize('original_str, capitalize_str',
                         [('skypro', 'Skypro'), ('sKYPRO', 'SKYPRO'), ('скайпро', 'Скайпро'),
                          ('', ''), (' ', ' '), ('1sky', '1sky')]
                         )
def test_string_capitalize(original_str, capitalize_str):
    string = StringUtils()
    assert string.capitilize(original_str) == capitalize_str


@pytest.mark.parametrize('original_str, trim_str',
                         [(' skypro', 'skypro'), ('  skypro', 'skypro'), (' 12345', '12345'),
                          ('sky pro', 'sky pro'), ('skypro ', 'skypro '), ('', ''), (' ', '')]
                         )
def test_string_trim(original_str, trim_str):
    string = StringUtils()
    assert string.trim(original_str) == trim_str


@pytest.mark.parametrize('original_str, delimiter, list_str',
                         [('1,2,3', ',', ['1', '2', '3']),
                          ('1:2:3', ':', ['1', '2', '3']),
                          ('1,2,3', ':', ['1,2,3']),
                          ('123', ':', ['123']),
                          ('', ':', [])]
                         )
def test_string_to_list(original_str, delimiter, list_str):
    string = StringUtils()
    assert string.to_list(original_str, delimiter) == list_str


@pytest.mark.parametrize('original_str, sym, res',
                         [('Skypro', 'S', True), ('Skypro', 'y', True), ('Skypro', 'o', True),
                          ('skypro', 'S', False), ('Skypro', 'U', False), ('', 'S', False)]
                         )
def test_string_contains(original_str, sym, res):
    string = StringUtils()
    assert string.contains(original_str, sym) == res


@pytest.mark.parametrize('original_str, sym, res_string',
                         [('skypro', 's', 'kypro'), ('skypro', 'u', 'skypro'), ('propro', 'o', 'prpr'),
                          ('', 's', ''), ('skypro', '', 'skypro'), ('', '', '')]
                         )
def test_string_delete_symbol(original_str, sym, res_string):
    string = StringUtils()
    assert string.delete_symbol(original_str, sym) == res_string


@pytest.mark.parametrize('original_str, sym, res',
                         [('Skypro', 'S', True), ('Skypro', 'y', False), ('skypro', 's', True),
                          ('skypro', 'S', False), ('skypro', '', True), ('', '', True)]
                         )
def test_string_starts_with(original_str, sym, res):
    string = StringUtils()
    assert string.starts_with(original_str, sym) == res


@pytest.mark.parametrize('original_str, sym, res',
                         [('Skypro', 'o', True), ('Skypro', 'y', False), ('skyprO', 'O', True),
                          ('skypro', 'O', False), ('skypro', '', True), ('', '', True)]
                         )
def test_string_enf_with(original_str, sym, res):
    string = StringUtils()
    assert string.end_with(original_str, sym) == res


@pytest.mark.parametrize('original_str, res',
                         [('', True), (' ', True), ('   ', True),
                          ('skypro', False)]
                         )
def test_string_is_empty(original_str, res):
    string = StringUtils()
    assert string.is_empty(original_str) == res


@pytest.mark.parametrize('original_lst, joiner, res_str',
                         [(['a', 'b', 'c'], ', ', 'a, b, c'), (['a', 'b', 'c'], ':', 'a:b:c'), ([], ':', '')]
                         )
def test_list_to_string(original_lst, joiner, res_str):
    string = StringUtils()
    assert string.list_to_string(original_lst, joiner) == res_str
