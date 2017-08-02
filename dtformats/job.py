# -*- coding: utf-8 -*-
"""Windows Task Scheduler job files."""

from __future__ import unicode_literals

from dtfabric.runtime import fabric as dtfabric_fabric

from dtformats import data_format


class WindowsTaskSchedularJobFile(data_format.BinaryDataFile):
  """Windows Task Scheduler job (.job) file."""

  # TODO: add format definition.
  # https://msdn.microsoft.com/en-us/library/cc248285.aspx

  _DATA_TYPE_FABRIC_DEFINITION = b'\n'.join([
      b'name: byte',
      b'type: integer',
      b'attributes:',
      b'  format: unsigned',
      b'  size: 1',
      b'  units: bytes',
      b'---',
      b'name: uint16',
      b'type: integer',
      b'attributes:',
      b'  format: unsigned',
      b'  size: 2',
      b'  units: bytes',
      b'---',
      b'name: uint32',
      b'type: integer',
      b'attributes:',
      b'  format: unsigned',
      b'  size: 4',
      b'  units: bytes',
      b'---',
      b'name: wchar16',
      b'type: character',
      b'attributes:',
      b'  size: 2',
      b'  units: bytes',
      b'---',
      b'name: system_time',
      b'type: structure',
      b'members:',
      b'- name: year',
      b'  data_type: uint16',
      b'- name: month',
      b'  data_type: uint16',
      b'- name: weekday',
      b'  data_type: uint16',
      b'- name: day_of_month',
      b'  data_type: uint16',
      b'- name: hours',
      b'  data_type: uint16',
      b'- name: minutes',
      b'  data_type: uint16',
      b'- name: seconds',
      b'  data_type: uint16',
      b'- name: milliseconds',
      b'  data_type: uint16',
      b'---',
      b'name: job_fixed_length_data_section',
      b'aliases: [FIXDLEN_DATA]',
      b'type: structure',
      b'urls: ["https://msdn.microsoft.com/en-us/library/cc248286.aspx"]',
      b'attributes:',
      b'  byte_order: little-endian',
      b'members:',
      b'- name: product_version',
      b'  data_type: uint16',
      b'- name: format_version',
      b'  data_type: uint16',
      b'- name: job_identifier',
      b'  type: uuid',
      b'- name: application_name_offset',
      b'  data_type: uint16',
      b'- name: triggers_offset',
      b'  data_type: uint16',
      b'- name: error_retry_count',
      b'  data_type: uint16',
      b'- name: error_retry_interval',
      b'  data_type: uint16',
      b'- name: idle_deadline',
      b'  data_type: uint16',
      b'- name: idle_wait',
      b'  data_type: uint16',
      b'- name: priority',
      b'  data_type: uint32',
      b'- name: maximum_run_time',
      b'  data_type: uint32',
      b'- name: exit_code',
      b'  data_type: uint32',
      b'- name: status',
      b'  data_type: uint32',
      b'- name: flags',
      b'  data_type: uint32',
      b'- name: last_run_time',
      b'  data_type: system_time',
      b'---',
      b'name: job_string',
      b'type: structure',
      b'urls: ["https://msdn.microsoft.com/en-us/library/cc248301.aspx"]',
      b'attributes:',
      b'  byte_order: little-endian',
      b'members:',
      b'- name: number_of_characters',
      b'  data_type: uint16',
      b'- name: string',
      b'  type: string',
      b'  encoding: utf-16-le',
      b'  element_data_type: wchar16',
      b'  number_of_elements: job_string.number_of_characters',
      b'---',
      b'name: job_user_data',
      b'type: structure',
      b'urls: ["https://msdn.microsoft.com/en-us/library/cc248306.aspx"]',
      b'attributes:',
      b'  byte_order: little-endian',
      b'members:',
      b'- name: size',
      b'  data_type: uint16',
      b'- name: stream',
      b'  type: stream',
      b'  element_data_type: byte',
      b'  elements_data_size: job_user_data.size',
      b'---',
      b'name: job_reserved_data',
      b'type: structure',
      b'urls: ["https://msdn.microsoft.com/en-us/library/cc248307.aspx"]',
      b'attributes:',
      b'  byte_order: little-endian',
      b'members:',
      b'- name: size',
      b'  data_type: uint16',
      b'- name: stream',
      b'  type: stream',
      b'  element_data_type: byte',
      b'  elements_data_size: job_reserved_data.size',
      b'---',
      b'name: job_trigger_date',
      b'type: structure',
      b'members:',
      b'- name: year',
      b'  data_type: uint16',
      b'- name: month',
      b'  data_type: uint16',
      b'- name: day_of_month',
      b'  data_type: uint16',
      b'---',
      b'name: job_trigger_time',
      b'type: structure',
      b'members:',
      b'- name: hours',
      b'  data_type: uint16',
      b'- name: minutes',
      b'  data_type: uint16',
      b'---',
      b'name: job_trigger',
      b'type: structure',
      b'attributes:',
      b'  byte_order: little-endian',
      b'members:',
      b'- name: size',
      b'  data_type: uint16',
      b'- name: reserved1',
      b'  data_type: uint16',
      b'- name: start_date',
      b'  data_type: job_trigger_date',
      b'- name: end_date',
      b'  data_type: job_trigger_date',
      b'- name: start_time',
      b'  data_type: job_trigger_time',
      b'- name: duration',
      b'  data_type: uint32',
      b'- name: interval',
      b'  data_type: uint32',
      b'- name: trigger_flags',
      b'  data_type: uint32',
      b'- name: trigger_type',
      b'  data_type: uint32',
      b'- name: trigger_arg0',
      b'  data_type: uint16',
      b'- name: trigger_arg1',
      b'  data_type: uint16',
      b'- name: trigger_arg2',
      b'  data_type: uint16',
      b'- name: trigger_padding',
      b'  data_type: uint16',
      b'- name: trigger_reserved2',
      b'  data_type: uint16',
      b'- name: trigger_reserved3',
      b'  data_type: uint16',
      b'---',
      b'name: job_triggers',
      b'type: structure',
      b'attributes:',
      b'  byte_order: little-endian',
      b'members:',
      b'- name: number_of_triggers',
      b'  data_type: uint16',
      b'- name: triggers_array',
      b'  type: sequence',
      b'  element_data_type: job_trigger',
      b'  number_of_elements: job_triggers.number_of_triggers',
      b'---',
      b'name: job_variable_length_data_section',
      b'type: structure',
      b'urls: ["https://msdn.microsoft.com/en-us/library/cc248287.aspx"]',
      b'attributes:',
      b'  byte_order: little-endian',
      b'members:',
      b'- name: running_instance_count',
      b'  data_type: uint16',
      b'- name: application_name',
      b'  data_type: job_string',
      b'- name: parameters',
      b'  data_type: job_string',
      b'- name: working_directory',
      b'  data_type: job_string',
      b'- name: author',
      b'  data_type: job_string',
      b'- name: comment',
      b'  data_type: job_string',
      b'- name: user_data',
      b'  data_type: job_user_data',
      b'- name: reserved_data',
      b'  data_type: job_reserved_data',
      b'- name: triggers',
      b'  data_type: job_triggers',
  ])

  # TODO: add job signature
  # https://msdn.microsoft.com/en-us/library/cc248299.aspx

  _DATA_TYPE_FABRIC = dtfabric_fabric.DataTypeFabric(
      yaml_definition=_DATA_TYPE_FABRIC_DEFINITION)

  _FIXED_LENGTH_DATA_SECTION = _DATA_TYPE_FABRIC.CreateDataTypeMap(
      'job_fixed_length_data_section')

  _FIXED_LENGTH_DATA_SECTION_SIZE = _FIXED_LENGTH_DATA_SECTION.GetByteSize()

  _VARIABLE_LENGTH_DATA_SECTION = _DATA_TYPE_FABRIC.CreateDataTypeMap(
      'job_variable_length_data_section')

  def _DebugPrintFixedLengthDataSection(self, data_section):
    """Prints fixed-length data section debug information.

    Args:
      data_section (job_fixed_length_data_section): fixed-length data section.
    """
    value_string = '0x{0:04x} ({1:d}.{2:d})'.format(
        data_section.product_version,
        (data_section.product_version >> 8) & 0xff,
        data_section.product_version & 0xff)
    self._DebugPrintValue('Product version', value_string)

    value_string = '{0:d}'.format(data_section.format_version)
    self._DebugPrintValue('Format version', value_string)

    value_string = '{0!s}'.format(data_section.job_identifier)
    self._DebugPrintValue('Job identifier', value_string)

    value_string = '0x{0:04x}'.format(data_section.application_name_offset)
    self._DebugPrintValue('Application name offset', value_string)

    value_string = '0x{0:04x}'.format(data_section.triggers_offset)
    self._DebugPrintValue('Triggers offset', value_string)

    value_string = '{0:d}'.format(data_section.error_retry_count)
    self._DebugPrintValue('Error retry count', value_string)

    value_string = '{0:d} minutes'.format(data_section.error_retry_interval)
    self._DebugPrintValue('Error retry interval', value_string)

    value_string = '{0:d} minutes'.format(data_section.idle_deadline)
    self._DebugPrintValue('Idle deadline', value_string)

    value_string = '{0:d} minutes'.format(data_section.idle_wait)
    self._DebugPrintValue('Idle wait', value_string)

    value_string = '0x{0:08x}'.format(data_section.priority)
    self._DebugPrintValue('Priority', value_string)

    value_string = '{0:d} milliseconds'.format(data_section.maximum_run_time)
    self._DebugPrintValue('Maximum run time', value_string)

    value_string = '0x{0:08x}'.format(data_section.exit_code)
    self._DebugPrintValue('Exit code', value_string)

    value_string = '0x{0:08x}'.format(data_section.status)
    self._DebugPrintValue('Status', value_string)

    value_string = '0x{0:08x}'.format(data_section.flags)
    self._DebugPrintValue('Flags', value_string)

    value_string = (
        '{0:04d}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}.{6:03d}').format(
            data_section.last_run_time.year,
            data_section.last_run_time.month,
            data_section.last_run_time.day_of_month,
            data_section.last_run_time.hours,
            data_section.last_run_time.minutes,
            data_section.last_run_time.seconds,
            data_section.last_run_time.milliseconds)
    self._DebugPrintValue('Last run time', value_string)

    self._DebugPrintText('\n')

  def _DebugPrintTrigger(self, trigger):
    """Prints trigger debug information.

    Args:
      trigger (job_trigger): trigger.
    """
    value_string = '{0:d}'.format(trigger.size)
    self._DebugPrintValue('Size', value_string)

    value_string = '0x{0:04x}'.format(trigger.reserved1)
    self._DebugPrintValue('Reserved1', value_string)

    value_string = '{0:04d}-{1:02d}-{2:02d}'.format(
        trigger.start_date.year, trigger.start_date.month,
        trigger.start_date.day_of_month)
    self._DebugPrintValue('Start date', value_string)

    value_string = '{0:04d}-{1:02d}-{2:02d}'.format(
        trigger.end_date.year, trigger.end_date.month,
        trigger.end_date.day_of_month)
    self._DebugPrintValue('End date', value_string)

    value_string = '{0:02d}:{1:02d}'.format(
        trigger.start_time.hours, trigger.start_time.minutes)
    self._DebugPrintValue('Start time', value_string)

    value_string = '{0:d} minutes'.format(trigger.duration)
    self._DebugPrintValue('Duration', value_string)

    value_string = '{0:d} minutes'.format(trigger.interval)
    self._DebugPrintValue('Interval', value_string)

    value_string = '0x{0:08x}'.format(trigger.trigger_flags)
    self._DebugPrintValue('Trigger flags', value_string)

    value_string = '0x{0:08x}'.format(trigger.trigger_type)
    self._DebugPrintValue('Trigger type', value_string)

    value_string = '0x{0:04x}'.format(trigger.trigger_arg0)
    self._DebugPrintValue('Trigger arg0', value_string)

    value_string = '0x{0:04x}'.format(trigger.trigger_arg1)
    self._DebugPrintValue('Trigger arg1', value_string)

    value_string = '0x{0:04x}'.format(trigger.trigger_arg2)
    self._DebugPrintValue('Trigger arg2', value_string)

    value_string = '0x{0:04x}'.format(trigger.trigger_padding)
    self._DebugPrintValue('Trigger padding', value_string)

    value_string = '0x{0:04x}'.format(trigger.trigger_reserved2)
    self._DebugPrintValue('Trigger reserved2', value_string)

    value_string = '0x{0:04x}'.format(trigger.trigger_reserved3)
    self._DebugPrintValue('Trigger reserved3', value_string)

    self._DebugPrintText('\n')

  def _DebugPrintVariableLengthDataSection(self, data_section):
    """Prints variable-length data section debug information.

    Args:
      data_section (job_variable_length_data_section): variable-length data
          section.
    """
    value_string = '{0:d}'.format(data_section.running_instance_count)
    self._DebugPrintValue('Running instance count', value_string)

    value_string = '({0:d}) {1:s}'.format(
        data_section.application_name.number_of_characters * 2,
        data_section.application_name.string)
    self._DebugPrintValue('Application name', value_string)

    value_string = '({0:d}) {1:s}'.format(
        data_section.parameters.number_of_characters * 2,
        data_section.parameters.string)
    self._DebugPrintValue('Parameters', value_string)

    value_string = '({0:d}) {1:s}'.format(
        data_section.working_directory.number_of_characters * 2,
        data_section.working_directory.string)
    self._DebugPrintValue('Working directory', value_string)

    value_string = '({0:d}) {1:s}'.format(
        data_section.author.number_of_characters * 2,
        data_section.author.string)
    self._DebugPrintValue('Author', value_string)

    value_string = '({0:d}) {1:s}'.format(
        data_section.comment.number_of_characters * 2,
        data_section.comment.string)
    self._DebugPrintValue('Comment', value_string)

    value_string = '{0:d}'.format(data_section.user_data.size)
    self._DebugPrintValue('User data size', value_string)
    self._DebugPrintData('User data', data_section.user_data.stream)

    value_string = '{0:d}'.format(data_section.reserved_data.size)
    self._DebugPrintValue('Reserved data size', value_string)
    self._DebugPrintData('Reserved data', data_section.reserved_data.stream)

    value_string = '{0:d}'.format(data_section.triggers.number_of_triggers)
    self._DebugPrintValue('Number of triggers', value_string)

    self._DebugPrintText('\n')

    for trigger in data_section.triggers.triggers_array:
      self._DebugPrintTrigger(trigger)

  def _ReadFixedLengthDataSection(self, file_object):
    """Reads the fixed-length data section.

    Args:
      file_object (file): file-like object.

    Raises:
      IOError: if the fixed-length data section cannot be read.
    """
    file_offset = file_object.tell()
    data_section = self._ReadStructure(
        file_object, file_offset, self._FIXED_LENGTH_DATA_SECTION_SIZE,
        self._FIXED_LENGTH_DATA_SECTION, 'fixed-length data section')

    if self._debug:
      self._DebugPrintFixedLengthDataSection(data_section)

  def _ReadVariableLengthDataSection(self, file_object):
    """Reads the variable-length data section.

    Args:
      file_object (file): file-like object.

    Raises:
      IOError: if the variable-length data section cannot be read.
    """
    file_offset = file_object.tell()
    data_size = self._file_size - file_offset
    data_section = self._ReadStructure(
        file_object, file_offset, data_size,
        self._VARIABLE_LENGTH_DATA_SECTION, 'variable-length data section')

    if self._debug:
      self._DebugPrintVariableLengthDataSection(data_section)

  def ReadFileObject(self, file_object):
    """Reads a Windows Task Scheduler job file-like object.

    Args:
      file_object (file): file-like object.

    Raises:
      ParseError: if the file cannot be read.
    """
    self._ReadFixedLengthDataSection(file_object)
    self._ReadVariableLengthDataSection(file_object)
