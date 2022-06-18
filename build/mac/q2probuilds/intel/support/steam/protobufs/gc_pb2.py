# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gc.proto',
  package='foobar',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x08gc.proto\x12\x06\x66oobar\"\xe8\x02\n\x12\x43MsgProtoBufHeader\x12\x17\n\x0f\x63lient_steam_id\x18\x01 \x01(\x06\x12\x19\n\x11\x63lient_session_id\x18\x02 \x01(\x05\x12\x15\n\rsource_app_id\x18\x03 \x01(\r\x12+\n\rjob_id_source\x18\n \x01(\x06:\x14\x31\x38\x34\x34\x36\x37\x34\x34\x30\x37\x33\x37\x30\x39\x35\x35\x31\x36\x31\x35\x12+\n\rjob_id_target\x18\x0b \x01(\x06:\x14\x31\x38\x34\x34\x36\x37\x34\x34\x30\x37\x33\x37\x30\x39\x35\x35\x31\x36\x31\x35\x12\x17\n\x0ftarget_job_name\x18\x0c \x01(\t\x12\x12\n\x07\x65result\x18\r \x01(\x05:\x01\x32\x12\x15\n\rerror_message\x18\x0e \x01(\t\x12K\n\ngc_msg_src\x18\xc8\x01 \x01(\x0e\x32\x18.foobar.GCProtoBufMsgSrc:\x1cGCProtoBufMsgSrc_Unspecified\x12\x1c\n\x13gc_dir_index_source\x18\xc9\x01 \x01(\r*\xb6\x01\n\x10GCProtoBufMsgSrc\x12 \n\x1cGCProtoBufMsgSrc_Unspecified\x10\x00\x12\x1f\n\x1bGCProtoBufMsgSrc_FromSystem\x10\x01\x12 \n\x1cGCProtoBufMsgSrc_FromSteamID\x10\x02\x12\x1b\n\x17GCProtoBufMsgSrc_FromGC\x10\x03\x12 \n\x1cGCProtoBufMsgSrc_ReplySystem\x10\x04')
)

_GCPROTOBUFMSGSRC = _descriptor.EnumDescriptor(
  name='GCProtoBufMsgSrc',
  full_name='foobar.GCProtoBufMsgSrc',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GCProtoBufMsgSrc_Unspecified', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GCProtoBufMsgSrc_FromSystem', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GCProtoBufMsgSrc_FromSteamID', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GCProtoBufMsgSrc_FromGC', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GCProtoBufMsgSrc_ReplySystem', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=384,
  serialized_end=566,
)
_sym_db.RegisterEnumDescriptor(_GCPROTOBUFMSGSRC)

GCProtoBufMsgSrc = enum_type_wrapper.EnumTypeWrapper(_GCPROTOBUFMSGSRC)
GCProtoBufMsgSrc_Unspecified = 0
GCProtoBufMsgSrc_FromSystem = 1
GCProtoBufMsgSrc_FromSteamID = 2
GCProtoBufMsgSrc_FromGC = 3
GCProtoBufMsgSrc_ReplySystem = 4



_CMSGPROTOBUFHEADER = _descriptor.Descriptor(
  name='CMsgProtoBufHeader',
  full_name='foobar.CMsgProtoBufHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_steam_id', full_name='foobar.CMsgProtoBufHeader.client_steam_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_session_id', full_name='foobar.CMsgProtoBufHeader.client_session_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_app_id', full_name='foobar.CMsgProtoBufHeader.source_app_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_id_source', full_name='foobar.CMsgProtoBufHeader.job_id_source', index=3,
      number=10, type=6, cpp_type=4, label=1,
      has_default_value=True, default_value=18446744073709551615,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_id_target', full_name='foobar.CMsgProtoBufHeader.job_id_target', index=4,
      number=11, type=6, cpp_type=4, label=1,
      has_default_value=True, default_value=18446744073709551615,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_job_name', full_name='foobar.CMsgProtoBufHeader.target_job_name', index=5,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eresult', full_name='foobar.CMsgProtoBufHeader.eresult', index=6,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='foobar.CMsgProtoBufHeader.error_message', index=7,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gc_msg_src', full_name='foobar.CMsgProtoBufHeader.gc_msg_src', index=8,
      number=200, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gc_dir_index_source', full_name='foobar.CMsgProtoBufHeader.gc_dir_index_source', index=9,
      number=201, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=381,
)

_CMSGPROTOBUFHEADER.fields_by_name['gc_msg_src'].enum_type = _GCPROTOBUFMSGSRC
DESCRIPTOR.message_types_by_name['CMsgProtoBufHeader'] = _CMSGPROTOBUFHEADER
DESCRIPTOR.enum_types_by_name['GCProtoBufMsgSrc'] = _GCPROTOBUFMSGSRC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CMsgProtoBufHeader = _reflection.GeneratedProtocolMessageType('CMsgProtoBufHeader', (_message.Message,), dict(
  DESCRIPTOR = _CMSGPROTOBUFHEADER,
  __module__ = 'gc_pb2'
  # @@protoc_insertion_point(class_scope:foobar.CMsgProtoBufHeader)
  ))
_sym_db.RegisterMessage(CMsgProtoBufHeader)


# @@protoc_insertion_point(module_scope)