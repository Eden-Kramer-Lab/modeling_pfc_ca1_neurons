#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 15:27:43 2018

@author: Mehrnoosh
"""
from loren_frank_data_processing import (get_interpolated_position_dataframe,
                                         get_LFP_dataframe,
                                         get_spike_indicator_dataframe,
                                         make_epochs_dataframe,
                                         make_neuron_dataframe,
                                         make_tetrode_dataframe)
from src.parameters import ANIMALS

days = range(1, N_DAYS + 1)
epoch_info = make_epochs_dataframe(ANIMALS, days)
tetrode_info = make_tetrode_dataframe(ANIMALS)

epoch_key = ('HPa', 6, 2)
tetrode_key = ('HPa',6,2,5)
neuron_info = make_neuron_dataframe(ANIMALS)
neuron_key = ('HPa', 6, 2, 5, 2)

spike = get_spike_indicator_dataframe(neuron_key, ANIMALS)
position_info = get_interpolated_position_dataframe(epoch_key, ANIMALS)
linear_distance = position_info['linear_distance']
x_pos = position_info['x_position']
y_pos = position_info['y_position']
speed = position_info['speed']
head_direction = position_info['head_direction']
eeg = get_LFP_dataframe(tetrode_key, ANIMALS)

linear_distance.to_csv('linear_distance.csv', sep=',')
spike.to_csv('spike.csv', sep=',')
x_pos.to_csv('x_position.csv', sep=',')
y_pos.to_csv('y_position.csv', sep=',')
head_direction.to_csv('direction.csv', sep=',')
speed.to_csv('speed.csv',sep=',')
eeg.to_csv('eeg.csv', sep=',')