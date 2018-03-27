# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class BBTools(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def run_RQCFilter_app(self, io_params, run_params, context=None):
        """
        :param io_params: instance of type "RQCFilterAppParams" (Parameters
           for the Narrative App version of RQCFilter. read_library_ref - UPA
           for the read library to filter. output_workspace_name - name of
           the workspace to put the output reads library and report.
           output_library_name - name of the Reads library object produced by
           the app.) -> structure: parameter "read_library_ref" of String,
           parameter "output_workspace_name" of String, parameter
           "output_library_name" of String
        :param run_params: instance of type "RQCFilterParams" (Contains all
           parameters for the RQCFilter program, EXCEPT for the inputs and
           outputs. Those are added specifically by each function. This lets
           us describe them separately for the local function that works
           mainly against the file system and the app that mainly works
           against the Workspace. This doesn't cover all of the 110+
           parameters provided by rqcfilter. Those not listed here are left
           as default values, except sketch=f (as that sends data to JGI
           servers for processing). Notes below are taken from the help
           output from rqcfilter.sh ver 37.90 Parameters (format = param name
           - default - description):
           --------------------------------------------------------- library
           - frag - should be one of 'frag', 'clip', 'lfpe', or 'clrs'.
           Adapter trimming parameters: ----------------------------
           trimfragadapter - f - Trim all known Illumina adapter sequences,
           including TruSeq and Nextera. Quality trimming parameters:
           ---------------------------- qtrim - f - Trim read ends to remove
           bases with quality below minq. Performed AFTER looking for kmers.
           Values: rl (trim both ends), f (neither end), r (right end only),
           l (left end only). trimq - 10 - Trim quality threshold.  Must also
           set qtrim for direction, will be ignored if qtrim=f maxns - 0 -
           Reads with more Ns than this will be discarded. minavgquality - 5
           - (maq) Reads with average quality (before trimming) below this
           will be discarded. minlength - 45 - (ml) Reads shorter than this
           after trimming will be discarded.  Pairs will be discarded only if
           both are shorter. mlf - 0.333 - (minlengthfraction) Reads shorter
           than this fraction of original length after trimming will be
           discarded. Mapping parameters (for vertebrate contaminants):
           ------------------------------------------------- removemouse - f
           - (mouse) Remove mouse reads via mapping. removecat - f - (cat)
           Remove cat reads via mapping. removedog - f - (dog) Remove dog
           reads via mapping. removehuman - f - (human) Remove human reads
           via mapping. Microbial contaminant removal parameters:
           ----------------------------------------- removemicrobes - f -
           (microbes) Remove common contaminant microbial reads via mapping,
           and place them in a separate file. taxlist - emptylist - (tax)
           Remove these taxa from the database before filtering.  Typically,
           this would be the organism name or NCBI ID, or a comma-delimited
           list.  Organism names should have underscores instead of spaces,
           such as Escherichia_coli. Filtering parameters (for artificial and
           microbial contaminants):
           -----------------------------------------------------------------
           rna - f - Remove reads containing RNA-specific artifacts. phix - t
           - Remove reads containing phiX kmers. Clumpify parameters:
           -------------------- clumpify - f - Run clumpify. dedupe - f -
           Remove duplicate reads. opticaldupes - f - Remove optical
           duplicates (Clumpify optical flag). Other processing parameters:
           ---------------------------- khist - f - Set to true to generate a
           kmer-frequency histogram of the output data. (included in report
           in the app, as a file in local function)) -> structure: parameter
           "library" of String, parameter "trimfragadapter" of type "boolean"
           (A boolean - 0 for false, 1 for true. @range (0, 1)), parameter
           "qtrim" of String, parameter "trimq" of Long, parameter "maxns" of
           Long, parameter "minavgquality" of Long, parameter "minlength" of
           Long, parameter "mlf" of Double, parameter "removemouse" of type
           "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1)),
           parameter "removecat" of type "boolean" (A boolean - 0 for false,
           1 for true. @range (0, 1)), parameter "removedog" of type
           "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1)),
           parameter "removehuman" of type "boolean" (A boolean - 0 for
           false, 1 for true. @range (0, 1)), parameter "removemicrobes" of
           type "boolean" (A boolean - 0 for false, 1 for true. @range (0,
           1)), parameter "taxlist" of list of String, parameter "rna" of
           type "boolean" (A boolean - 0 for false, 1 for true. @range (0,
           1)), parameter "phix" of type "boolean" (A boolean - 0 for false,
           1 for true. @range (0, 1)), parameter "clumpify" of type "boolean"
           (A boolean - 0 for false, 1 for true. @range (0, 1)), parameter
           "dedupe" of type "boolean" (A boolean - 0 for false, 1 for true.
           @range (0, 1)), parameter "opticaldupes" of type "boolean" (A
           boolean - 0 for false, 1 for true. @range (0, 1)), parameter
           "khist" of type "boolean" (A boolean - 0 for false, 1 for true.
           @range (0, 1))
        :returns: instance of type "RQCFilterAppOutput" -> structure:
           parameter "report_name" of String, parameter "report_ref" of String
        """
        return self._client.call_method(
            'BBTools.run_RQCFilter_app',
            [io_params, run_params], self._service_ver, context)

    def run_RQCFilter_local(self, io_params, run_params, context=None):
        """
        :param io_params: instance of type "RQCFilterLocalParams" (Parameters
           for local version of RQCFilter. read_library_ref - UPA for the
           read library to filter. -OR- reads_file - path to the reads file
           to filter. Expects an interleaved file, if it's paired end. If
           both of the above are given, the read_library_ref takes
           precedence.) -> structure: parameter "read_library_ref" of String,
           parameter "reads_file" of String
        :param run_params: instance of type "RQCFilterParams" (Contains all
           parameters for the RQCFilter program, EXCEPT for the inputs and
           outputs. Those are added specifically by each function. This lets
           us describe them separately for the local function that works
           mainly against the file system and the app that mainly works
           against the Workspace. This doesn't cover all of the 110+
           parameters provided by rqcfilter. Those not listed here are left
           as default values, except sketch=f (as that sends data to JGI
           servers for processing). Notes below are taken from the help
           output from rqcfilter.sh ver 37.90 Parameters (format = param name
           - default - description):
           --------------------------------------------------------- library
           - frag - should be one of 'frag', 'clip', 'lfpe', or 'clrs'.
           Adapter trimming parameters: ----------------------------
           trimfragadapter - f - Trim all known Illumina adapter sequences,
           including TruSeq and Nextera. Quality trimming parameters:
           ---------------------------- qtrim - f - Trim read ends to remove
           bases with quality below minq. Performed AFTER looking for kmers.
           Values: rl (trim both ends), f (neither end), r (right end only),
           l (left end only). trimq - 10 - Trim quality threshold.  Must also
           set qtrim for direction, will be ignored if qtrim=f maxns - 0 -
           Reads with more Ns than this will be discarded. minavgquality - 5
           - (maq) Reads with average quality (before trimming) below this
           will be discarded. minlength - 45 - (ml) Reads shorter than this
           after trimming will be discarded.  Pairs will be discarded only if
           both are shorter. mlf - 0.333 - (minlengthfraction) Reads shorter
           than this fraction of original length after trimming will be
           discarded. Mapping parameters (for vertebrate contaminants):
           ------------------------------------------------- removemouse - f
           - (mouse) Remove mouse reads via mapping. removecat - f - (cat)
           Remove cat reads via mapping. removedog - f - (dog) Remove dog
           reads via mapping. removehuman - f - (human) Remove human reads
           via mapping. Microbial contaminant removal parameters:
           ----------------------------------------- removemicrobes - f -
           (microbes) Remove common contaminant microbial reads via mapping,
           and place them in a separate file. taxlist - emptylist - (tax)
           Remove these taxa from the database before filtering.  Typically,
           this would be the organism name or NCBI ID, or a comma-delimited
           list.  Organism names should have underscores instead of spaces,
           such as Escherichia_coli. Filtering parameters (for artificial and
           microbial contaminants):
           -----------------------------------------------------------------
           rna - f - Remove reads containing RNA-specific artifacts. phix - t
           - Remove reads containing phiX kmers. Clumpify parameters:
           -------------------- clumpify - f - Run clumpify. dedupe - f -
           Remove duplicate reads. opticaldupes - f - Remove optical
           duplicates (Clumpify optical flag). Other processing parameters:
           ---------------------------- khist - f - Set to true to generate a
           kmer-frequency histogram of the output data. (included in report
           in the app, as a file in local function)) -> structure: parameter
           "library" of String, parameter "trimfragadapter" of type "boolean"
           (A boolean - 0 for false, 1 for true. @range (0, 1)), parameter
           "qtrim" of String, parameter "trimq" of Long, parameter "maxns" of
           Long, parameter "minavgquality" of Long, parameter "minlength" of
           Long, parameter "mlf" of Double, parameter "removemouse" of type
           "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1)),
           parameter "removecat" of type "boolean" (A boolean - 0 for false,
           1 for true. @range (0, 1)), parameter "removedog" of type
           "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1)),
           parameter "removehuman" of type "boolean" (A boolean - 0 for
           false, 1 for true. @range (0, 1)), parameter "removemicrobes" of
           type "boolean" (A boolean - 0 for false, 1 for true. @range (0,
           1)), parameter "taxlist" of list of String, parameter "rna" of
           type "boolean" (A boolean - 0 for false, 1 for true. @range (0,
           1)), parameter "phix" of type "boolean" (A boolean - 0 for false,
           1 for true. @range (0, 1)), parameter "clumpify" of type "boolean"
           (A boolean - 0 for false, 1 for true. @range (0, 1)), parameter
           "dedupe" of type "boolean" (A boolean - 0 for false, 1 for true.
           @range (0, 1)), parameter "opticaldupes" of type "boolean" (A
           boolean - 0 for false, 1 for true. @range (0, 1)), parameter
           "khist" of type "boolean" (A boolean - 0 for false, 1 for true.
           @range (0, 1))
        :returns: instance of type "RQCFilterLocalOutput" (The output from
           the local function version of RQCFilter. output_directory: the
           path to the output directory containing all files generated by
           RQCFilter. run_log: the path to the run log from RQCFilter (i.e.
           its stderr). This will be a path in the output directory, added
           separately here for convenience. filtered_fastq_file: the path to
           the file (in the output directory) containing the filtered FASTQ
           reads. This will likely be compressed, if you need it
           decompressed, you can use DataFileUtil.unpack_file (see that
           module).) -> structure: parameter "output_directory" of String,
           parameter "run_log" of String, parameter "filtered_fastq_file" of
           String
        """
        return self._client.call_method(
            'BBTools.run_RQCFilter_local',
            [io_params, run_params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('BBTools.status',
                                        [], self._service_ver, context)
