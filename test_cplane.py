#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
###
# Name: Kristaaaa, Atabak
# Student ID: KristaIDHere, AtabakIDHere
# Email:  kristaEmailHere , AtabakEmail
# Course: CS510 Fall 2017
# Assignment: Classwork 5
###
"""
import cplane


def test_plane():
    """
    test function
    :return:
    :rtype:
    """
    c_plane = cplane.ListComplexPlane(0, 3, 3, 0, 3, 3)
    assert c_plane.plane == [[0.0, 0j], [0.0, 1.5j], [0.0, 3j], [1.5, 0j],
                             [1.5, 1.5j], [1.5, 3j], [3.0, 0j], [3.0, 1.5j], [3.0, 3j]]
