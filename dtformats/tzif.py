# -*- coding: utf-8 -*-
"""Timezone information files (TZif)."""

from dtfabric.runtime import data_maps as dtfabric_data_maps

from dtformats import data_format
from dtformats import errors


class TimeZoneInformationFile(data_format.BinaryDataFile):
  """Timezone information file (TZif).

  Attributes:
    format_version (int): format version.
  """

  # Using a class constant significantly speeds up the time required to load
  # the dtFabric definition file.
  _FABRIC = data_format.BinaryDataFile.ReadDefinitionFile('tzif.yaml')

  # TODO: move path into structure.

  _FILE_SIGNATURE = b'TZif'

  def __init__(self, debug=False, output_writer=None):
    """Initializes a timezone information file.

    Args:
      debug (Optional[bool]): True if debug information should be written.
      output_writer (Optional[OutputWriter]): output writer.
    """
    super(TimeZoneInformationFile, self).__init__(
        debug=debug, output_writer=output_writer)
    self.format_version = None

  def _DebugPrintFileHeader(self, file_header):
    """Prints file header debug information.

    Args:
      file_header (tzif_file_header): file header.
    """
    value_string = '{0!s}'.format(file_header.signature)
    self._DebugPrintValue('Signature', value_string)

    value_string = '0x{0:02x}'.format(file_header.format_version)
    self._DebugPrintValue('Format version', value_string)

    self._DebugPrintData('Unknown1', file_header.unknown1)

    value_string = '{0:d}'.format(file_header.number_of_utc_time_indicators)
    self._DebugPrintValue('Number of UTC time indicators', value_string)

    value_string = '{0:d}'.format(
        file_header.number_of_standard_time_indicators)
    self._DebugPrintValue('Number of standard time indicators', value_string)

    value_string = '{0:d}'.format(file_header.number_of_leap_seconds)
    self._DebugPrintValue('Number of leap seconds', value_string)

    value_string = '{0:d}'.format(file_header.number_of_transition_times)
    self._DebugPrintValue('Number of transition times', value_string)

    value_string = '{0:d}'.format(file_header.number_of_local_time_types)
    self._DebugPrintValue('Number of local time types', value_string)

    value_string = '{0:d}'.format(
        file_header.timezone_abbreviation_strings_size)
    self._DebugPrintValue('Timezone abbreviation strings size', value_string)

    self._DebugPrintText('\n')

  def _DebugPrintTransitionTimeIndex(self, transition_time_index):
    """Prints transition time index debug information.

    Args:
      transition_time_index (tzif_transition_time_index): transition time index.
    """
    for index, type_of_localtime in enumerate(transition_time_index):
      description_string = 'Type of local time: {0:d}'.format(index)
      value_string = '{0:d}'.format(type_of_localtime)
      self._DebugPrintValue(description_string, value_string)

    self._DebugPrintText('\n')

  def _DebugPrintTransitionTimes(self, transition_times):
    """Prints transition times debug information.

    Args:
      transition_times (tzif_transition_times): transition times.
    """
    for index, transition_time in enumerate(transition_times):
      description_string = 'Transition time: {0:d}'.format(index)
      value_string = '{0:d}'.format(transition_time)
      self._DebugPrintValue(description_string, value_string)

    self._DebugPrintText('\n')

  def _ReadFileHeader(self, file_object):
    """Reads a file header.

    Args:
      file_object (file): file-like object.

    Returns:
      tzif_file_header: a file header.

    Raises:
      ParseError: if the file header cannot be read.
    """
    data_type_map = self._GetDataTypeMap('tzif_file_header')

    file_header, _ = self._ReadStructureFromFileObject(
        file_object, 0, data_type_map, 'file header')

    if self._debug:
      self._DebugPrintFileHeader(file_header)

    if file_header.signature != self._FILE_SIGNATURE:
      raise errors.ParseError('Unsupported file signature.')

    if file_header.format_version not in (0x00, 0x32, 0x33):
      raise errors.ParseError('Unsupported format version: {0:d}.'.format(
          file_header.format_version))

    return file_header

  def _ReadLeapSecondRecords(self, file_object, file_header):
    """Reads the lead second records.

    Args:
      file_object (file): file-like object.
      file_header (tzif_file_header): file header.

    Raises:
      ParseError: if the leap second records cannot be read.
    """
    file_offset = file_object.tell()
    data_size = 8 * file_header.number_of_leap_seconds

    data = self._ReadData(
        file_object, file_offset, data_size, 'leap second records')

    if self._debug:
      self._DebugPrintData('Leap second records data', data)

  def _ReadLocalTimeTypesTable(self, file_object, file_header):
    """Reads the local time types table.

    Args:
      file_object (file): file-like object.
      file_header (tzif_file_header): file header.

    Raises:
      ParseError: if the local time types table cannot be read.
    """
    file_offset = file_object.tell()
    # ttinfo structure
    data_size = 6 * file_header.number_of_local_time_types

    data = self._ReadData(
        file_object, file_offset, data_size, 'local time types table')

    if self._debug:
      self._DebugPrintData('Local time types table data', data)

  def _ReadStandardTimeIndicators(self, file_object, file_header):
    """Reads the standard time indicators.

    Args:
      file_object (file): file-like object.
      file_header (tzif_file_header): file header.

    Raises:
      ParseError: if the standard time indicators cannot be read.
    """
    file_offset = file_object.tell()
    data_size = 1 * file_header.number_of_standard_time_indicators

    data = self._ReadData(
        file_object, file_offset, data_size, 'standard time indicators')

    if self._debug:
      self._DebugPrintData('Standard time indicators data', data)

  def _ReadTransitionTimeIndex(self, file_object, file_header):
    """Reads transition time index.

    Args:
      file_object (file): file-like object.
      file_header (tzif_file_header): file header.

    Raises:
      ParseError: if the transition time index cannot be read.
    """
    file_offset = file_object.tell()
    data_type_map = self._GetDataTypeMap('tzif_transition_time_index')

    data_size = 1 * file_header.number_of_transition_times

    data = self._ReadData(
        file_object, file_offset, data_size, 'transition time index')

    context = dtfabric_data_maps.DataTypeMapContext(values={
        'tzif_file_header': file_header})

    try:
      transition_time_index = self._ReadStructureFromByteStream(
          data, file_offset, data_type_map, 'transition time index',
          context=context)
    except (ValueError, errors.ParseError) as exception:
      raise errors.ParseError((
          'Unable to parse transition time index value with error: '
          '{0!s}').format(exception))

    if self._debug:
      self._DebugPrintTransitionTimeIndex(transition_time_index)

  def _ReadTimezoneAbbreviationStrings(self, file_object, file_header):
    """Reads timezone abbreviation strings.

    Args:
      file_object (file): file-like object.
      file_header (tzif_file_header): file header.

    Raises:
      ParseError: if the timezone abbreviation strings cannot be read.
    """
    file_offset = file_object.tell()

    data = self._ReadData(
        file_object, file_offset,
        file_header.timezone_abbreviation_strings_size,
        'timezeone abbreviation strings')

    if self._debug:
      self._DebugPrintData('Timezeone abbreviation strings data', data)

  def _ReadTimezoneInformation32bit(self, file_object):
    """Reads 32-bit timezone information.

    Args:
      file_object (file): file-like object.

    Raises:
      ParseError: if the 32-bit timezone information cannot be read.
    """
    file_header = self._ReadFileHeader(file_object)

    self.format_version = file_header.format_version

    self._ReadTransitionTimes32bit(file_object, file_header)
    self._ReadTransitionTimeIndex(file_object, file_header)
    self._ReadLocalTimeTypesTable(file_object, file_header)
    self._ReadTimezoneAbbreviationStrings(file_object, file_header)
    self._ReadLeapSecondRecords(file_object, file_header)
    self._ReadStandardTimeIndicators(file_object, file_header)
    self._ReadUTCTimeIndicators(file_object, file_header)

  def _ReadTimezoneInformation64bit(self, file_object):
    """Reads 64-bit timezone information.

    Args:
      file_object (file): file-like object.

    Raises:
      ParseError: if the 64-bit timezone information cannot be read.
    """
    file_header = self._ReadFileHeader(file_object)

    self._ReadTransitionTimes64bit(file_object, file_header)
    self._ReadTransitionTimeIndex(file_object, file_header)
    self._ReadLocalTimeTypesTable(file_object, file_header)
    self._ReadTimezoneAbbreviationStrings(file_object, file_header)
    self._ReadLeapSecondRecords(file_object, file_header)
    self._ReadStandardTimeIndicators(file_object, file_header)
    self._ReadUTCTimeIndicators(file_object, file_header)

  def _ReadTransitionTimes32bit(self, file_object, file_header):
    """Reads 32-bit transition times.

    Args:
      file_object (file): file-like object.
      file_header (tzif_file_header): file header.

    Raises:
      ParseError: if the 32-bit transition times cannot be read.
    """
    file_offset = file_object.tell()
    data_type_map = self._GetDataTypeMap('tzif_transition_times_32bit')

    data_size = 4 * file_header.number_of_transition_times

    data = self._ReadData(
        file_object, file_offset, data_size, '32-bit transition times')

    context = dtfabric_data_maps.DataTypeMapContext(values={
        'tzif_file_header': file_header})

    try:
      transition_times = self._ReadStructureFromByteStream(
          data, file_offset, data_type_map, '32-bit transition times',
          context=context)
    except (ValueError, errors.ParseError) as exception:
      raise errors.ParseError((
          'Unable to parse 32-bit transition times value with error: '
          '{0!s}').format(exception))

    if self._debug:
      self._DebugPrintTransitionTimes(transition_times)

  def _ReadTransitionTimes64bit(self, file_object, file_header):
    """Reads 64-bit transition times.

    Args:
      file_object (file): file-like object.
      file_header (tzif_file_header): file header.

    Raises:
      ParseError: if the 64-bit transition times cannot be read.
    """
    file_offset = file_object.tell()
    data_type_map = self._GetDataTypeMap('tzif_transition_times_64bit')

    data_size = 8 * file_header.number_of_transition_times

    data = self._ReadData(
        file_object, file_offset, data_size, '64-bit transition times')

    context = dtfabric_data_maps.DataTypeMapContext(values={
        'tzif_file_header': file_header})

    try:
      transition_times = self._ReadStructureFromByteStream(
          data, file_offset, data_type_map, '64-bit transition times',
          context=context)
    except (ValueError, errors.ParseError) as exception:
      raise errors.ParseError((
          'Unable to parse 64-bit transition times value with error: '
          '{0!s}').format(exception))

    if self._debug:
      self._DebugPrintTransitionTimes(transition_times)

  def _ReadUTCTimeIndicators(self, file_object, file_header):
    """Reads the UTC time indicators.

    Args:
      file_object (file): file-like object.
      file_header (tzif_file_header): file header.

    Raises:
      ParseError: if the UTC time indicators cannot be read.
    """
    file_offset = file_object.tell()
    data_size = 1 * file_header.number_of_utc_time_indicators

    data = self._ReadData(
        file_object, file_offset, data_size, 'UTC time indicators')

    if self._debug:
      self._DebugPrintData('UTC time indicators data', data)

  def ReadFileObject(self, file_object):
    """Reads a timezone information file-like object.

    Args:
      file_object (file): file-like object.

    Raises:
      ParseError: if the file cannot be read.
    """
    self._ReadTimezoneInformation32bit(file_object)

    if self.format_version in (0x32, 0x33):
      self._ReadTimezoneInformation64bit(file_object)

      data = file_object.read()

      if self._debug:
        self._DebugPrintData('Timezone string', data)
