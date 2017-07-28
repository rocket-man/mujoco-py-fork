from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path
import tensorflow as tf

data_files_path = tf.resource_loader.get_data_files_path()
_op_module = tf.load_op_library(
    os.path.join(data_files_path, 'cuda_buffer_ops.so'))

read_cuda_buffer_uint8_op = _op_module.read_cuda_buffer_uint8
read_cuda_buffer_uint16_op = _op_module.read_cuda_buffer_uint16
read_cuda_buffer_float_op = _op_module.read_cuda_buffer_float