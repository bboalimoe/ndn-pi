# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='configure-device.proto',
  package='',
  serialized_pb='\n\x16\x63onfigure-device.proto\"\x8e\x02\n\x1a\x44\x65viceConfigurationMessage\x12G\n\rconfiguration\x18\xe4\x01 \x02(\x0b\x32/.DeviceConfigurationMessage.DeviceConfiguration\x1a\x1a\n\x04Name\x12\x12\n\ncomponents\x18\x08 \x03(\x0c\x1a\x8a\x01\n\x13\x44\x65viceConfiguration\x12\x38\n\rnetworkPrefix\x18\xe2\x01 \x02(\x0b\x32 .DeviceConfigurationMessage.Name\x12\x39\n\x0e\x63ontrollerName\x18\xe3\x01 \x02(\x0b\x32 .DeviceConfigurationMessage.Name')




_DEVICECONFIGURATIONMESSAGE_NAME = descriptor.Descriptor(
  name='Name',
  full_name='DeviceConfigurationMessage.Name',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='components', full_name='DeviceConfigurationMessage.Name.components', index=0,
      number=8, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=130,
  serialized_end=156,
)

_DEVICECONFIGURATIONMESSAGE_DEVICECONFIGURATION = descriptor.Descriptor(
  name='DeviceConfiguration',
  full_name='DeviceConfigurationMessage.DeviceConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='networkPrefix', full_name='DeviceConfigurationMessage.DeviceConfiguration.networkPrefix', index=0,
      number=226, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='controllerName', full_name='DeviceConfigurationMessage.DeviceConfiguration.controllerName', index=1,
      number=227, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=159,
  serialized_end=297,
)

_DEVICECONFIGURATIONMESSAGE = descriptor.Descriptor(
  name='DeviceConfigurationMessage',
  full_name='DeviceConfigurationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='configuration', full_name='DeviceConfigurationMessage.configuration', index=0,
      number=228, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DEVICECONFIGURATIONMESSAGE_NAME, _DEVICECONFIGURATIONMESSAGE_DEVICECONFIGURATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=27,
  serialized_end=297,
)

_DEVICECONFIGURATIONMESSAGE_NAME.containing_type = _DEVICECONFIGURATIONMESSAGE;
_DEVICECONFIGURATIONMESSAGE_DEVICECONFIGURATION.fields_by_name['networkPrefix'].message_type = _DEVICECONFIGURATIONMESSAGE_NAME
_DEVICECONFIGURATIONMESSAGE_DEVICECONFIGURATION.fields_by_name['controllerName'].message_type = _DEVICECONFIGURATIONMESSAGE_NAME
_DEVICECONFIGURATIONMESSAGE_DEVICECONFIGURATION.containing_type = _DEVICECONFIGURATIONMESSAGE;
_DEVICECONFIGURATIONMESSAGE.fields_by_name['configuration'].message_type = _DEVICECONFIGURATIONMESSAGE_DEVICECONFIGURATION
DESCRIPTOR.message_types_by_name['DeviceConfigurationMessage'] = _DEVICECONFIGURATIONMESSAGE

class DeviceConfigurationMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Name(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _DEVICECONFIGURATIONMESSAGE_NAME
    
    # @@protoc_insertion_point(class_scope:DeviceConfigurationMessage.Name)
  
  class DeviceConfiguration(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _DEVICECONFIGURATIONMESSAGE_DEVICECONFIGURATION
    
    # @@protoc_insertion_point(class_scope:DeviceConfigurationMessage.DeviceConfiguration)
  DESCRIPTOR = _DEVICECONFIGURATIONMESSAGE
  
  # @@protoc_insertion_point(class_scope:DeviceConfigurationMessage)

# @@protoc_insertion_point(module_scope)
