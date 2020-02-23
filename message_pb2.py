# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='message',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rmessage.proto\x12\x07message\"-\n\x17InsertTrajectoryRequest\x12\x12\n\ntrajectory\x18\x01 \x01(\t\"(\n\x15InsertTrajectoryReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x12\n\x10GetParamsRequest\"\r\n\x0bQuitRequest\"\x0b\n\tQuitReply\"5\n\x0eGetParamsReply\x12\x13\n\x0b\x66rame_count\x18\x01 \x01(\x05\x12\x0e\n\x06params\x18\x02 \x01(\t2\xdc\x01\n\x0bInformation\x12V\n\x10InsertTrajectory\x12 .message.InsertTrajectoryRequest\x1a\x1e.message.InsertTrajectoryReply\"\x00\x12\x41\n\tGetParams\x12\x19.message.GetParamsRequest\x1a\x17.message.GetParamsReply\"\x00\x12\x32\n\x04Quit\x12\x14.message.QuitRequest\x1a\x12.message.QuitReply\"\x00\x62\x06proto3'
)




_INSERTTRAJECTORYREQUEST = _descriptor.Descriptor(
  name='InsertTrajectoryRequest',
  full_name='message.InsertTrajectoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trajectory', full_name='message.InsertTrajectoryRequest.trajectory', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=71,
)


_INSERTTRAJECTORYREPLY = _descriptor.Descriptor(
  name='InsertTrajectoryReply',
  full_name='message.InsertTrajectoryReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='message.InsertTrajectoryReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=113,
)


_GETPARAMSREQUEST = _descriptor.Descriptor(
  name='GetParamsRequest',
  full_name='message.GetParamsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=133,
)


_QUITREQUEST = _descriptor.Descriptor(
  name='QuitRequest',
  full_name='message.QuitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=148,
)


_QUITREPLY = _descriptor.Descriptor(
  name='QuitReply',
  full_name='message.QuitReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=161,
)


_GETPARAMSREPLY = _descriptor.Descriptor(
  name='GetParamsReply',
  full_name='message.GetParamsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_count', full_name='message.GetParamsReply.frame_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='message.GetParamsReply.params', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=216,
)

DESCRIPTOR.message_types_by_name['InsertTrajectoryRequest'] = _INSERTTRAJECTORYREQUEST
DESCRIPTOR.message_types_by_name['InsertTrajectoryReply'] = _INSERTTRAJECTORYREPLY
DESCRIPTOR.message_types_by_name['GetParamsRequest'] = _GETPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QuitRequest'] = _QUITREQUEST
DESCRIPTOR.message_types_by_name['QuitReply'] = _QUITREPLY
DESCRIPTOR.message_types_by_name['GetParamsReply'] = _GETPARAMSREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InsertTrajectoryRequest = _reflection.GeneratedProtocolMessageType('InsertTrajectoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _INSERTTRAJECTORYREQUEST,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.InsertTrajectoryRequest)
  })
_sym_db.RegisterMessage(InsertTrajectoryRequest)

InsertTrajectoryReply = _reflection.GeneratedProtocolMessageType('InsertTrajectoryReply', (_message.Message,), {
  'DESCRIPTOR' : _INSERTTRAJECTORYREPLY,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.InsertTrajectoryReply)
  })
_sym_db.RegisterMessage(InsertTrajectoryReply)

GetParamsRequest = _reflection.GeneratedProtocolMessageType('GetParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPARAMSREQUEST,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.GetParamsRequest)
  })
_sym_db.RegisterMessage(GetParamsRequest)

QuitRequest = _reflection.GeneratedProtocolMessageType('QuitRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUITREQUEST,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.QuitRequest)
  })
_sym_db.RegisterMessage(QuitRequest)

QuitReply = _reflection.GeneratedProtocolMessageType('QuitReply', (_message.Message,), {
  'DESCRIPTOR' : _QUITREPLY,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.QuitReply)
  })
_sym_db.RegisterMessage(QuitReply)

GetParamsReply = _reflection.GeneratedProtocolMessageType('GetParamsReply', (_message.Message,), {
  'DESCRIPTOR' : _GETPARAMSREPLY,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.GetParamsReply)
  })
_sym_db.RegisterMessage(GetParamsReply)



_INFORMATION = _descriptor.ServiceDescriptor(
  name='Information',
  full_name='message.Information',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=219,
  serialized_end=439,
  methods=[
  _descriptor.MethodDescriptor(
    name='InsertTrajectory',
    full_name='message.Information.InsertTrajectory',
    index=0,
    containing_service=None,
    input_type=_INSERTTRAJECTORYREQUEST,
    output_type=_INSERTTRAJECTORYREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetParams',
    full_name='message.Information.GetParams',
    index=1,
    containing_service=None,
    input_type=_GETPARAMSREQUEST,
    output_type=_GETPARAMSREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Quit',
    full_name='message.Information.Quit',
    index=2,
    containing_service=None,
    input_type=_QUITREQUEST,
    output_type=_QUITREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INFORMATION)

DESCRIPTOR.services_by_name['Information'] = _INFORMATION

# @@protoc_insertion_point(module_scope)
