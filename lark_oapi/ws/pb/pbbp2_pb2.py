# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pbbp2.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

from . import gogo_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='pbbp2.proto',
    package='pbbp2',
    syntax='proto2',
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0bpbbp2.proto\x12\x05pbbp2\x1a\ngogo.proto\"$\n\x06Header\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"\xbf\x01\n\x05\x46rame\x12\r\n\x05SeqID\x18\x01 \x02(\x04\x12\r\n\x05LogID\x18\x02 \x02(\x04\x12\x0f\n\x07service\x18\x03 \x02(\x05\x12\x0e\n\x06method\x18\x04 \x02(\x05\x12$\n\x07headers\x18\x05 \x03(\x0b\x32\r.pbbp2.HeaderB\x04\xc8\xde\x1f\x00\x12\x18\n\x10payload_encoding\x18\x06 \x01(\t\x12\x14\n\x0cpayload_type\x18\x07 \x01(\t\x12\x0f\n\x07payload\x18\x08 \x01(\x0c\x12\x10\n\x08LogIDNew\x18\t \x01(\t'
    ,
    dependencies=[gogo_pb2.DESCRIPTOR, ])

_HEADER = _descriptor.Descriptor(
    name='Header',
    full_name='pbbp2.Header',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='pbbp2.Header.key', index=0,
            number=1, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='value', full_name='pbbp2.Header.value', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
    serialized_start=34,
    serialized_end=70,
)

_FRAME = _descriptor.Descriptor(
    name='Frame',
    full_name='pbbp2.Frame',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='SeqID', full_name='pbbp2.Frame.SeqID', index=0,
            number=1, type=4, cpp_type=4, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='LogID', full_name='pbbp2.Frame.LogID', index=1,
            number=2, type=4, cpp_type=4, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='service', full_name='pbbp2.Frame.service', index=2,
            number=3, type=5, cpp_type=1, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='method', full_name='pbbp2.Frame.method', index=3,
            number=4, type=5, cpp_type=1, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='headers', full_name='pbbp2.Frame.headers', index=4,
            number=5, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=b'\310\336\037\000', file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='payload_encoding', full_name='pbbp2.Frame.payload_encoding', index=5,
            number=6, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='payload_type', full_name='pbbp2.Frame.payload_type', index=6,
            number=7, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='payload', full_name='pbbp2.Frame.payload', index=7,
            number=8, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=b"",
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='LogIDNew', full_name='pbbp2.Frame.LogIDNew', index=8,
            number=9, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
    serialized_start=73,
    serialized_end=264,
)

_FRAME.fields_by_name['headers'].message_type = _HEADER
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Frame'] = _FRAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
    'DESCRIPTOR': _HEADER,
    '__module__': 'pbbp2_pb2'
    # @@protoc_insertion_point(class_scope:pbbp2.Header)
})
_sym_db.RegisterMessage(Header)

Frame = _reflection.GeneratedProtocolMessageType('Frame', (_message.Message,), {
    'DESCRIPTOR': _FRAME,
    '__module__': 'pbbp2_pb2'
    # @@protoc_insertion_point(class_scope:pbbp2.Frame)
})
_sym_db.RegisterMessage(Frame)

_FRAME.fields_by_name['headers']._options = None
# @@protoc_insertion_point(module_scope)