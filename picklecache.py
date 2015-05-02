#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK13 synthesizing tasks - Using pickle to manipulate files."""


import os
import pickle


class PickleCache(object):
    """A custom made class."""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor for the PickleCache class.

        Args:
            file_path(string, optional): Defaults to datastore.pkl.
            autosync(bool, optional): Defaults to False.

        Example:
            >>> cacher = PickleCache()
            >>> kprint cacher._PickleCache__file_path
            'datastore.pkl'
            >>> print cacher._PickleCache__data
            {}

        """
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """A magical method to make our cache behave like a dictionary.

        Args:
            key(string, required): A required input.
            value(string, required): A required input.

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'

        """

        self.__data[key] = value
        if self.autosync:
            self.flush()

    def __len__(self):
        """A function to check the lenght of __data.

        Example:
            >>> len(pcache)
            1

        """

        return len(self.__data)

    def __getitem__(self, key):
        """A function to retrieve data.

        Args:
            key(string, required): A required input.

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'

        """

        return self.__data[key]

    def __delitem__(self, key):
        """A function to delete items.

        Args:
            key (string, required): A required input.

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print len(pcache)
            1
            >>> del pcache['test']
            >>> print len(pcache)
            0

        """

        del self.__data[key]
        if self.autosync:
            self.flush()

    def load(self):
        """A function to load an existing file."""

        if os.path.exists(self.__file_path) and \
           os.path.getsize(self.__file_path) > 0:
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """A function to write data to a file."""

        fhandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
