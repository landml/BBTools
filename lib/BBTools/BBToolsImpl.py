# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os

from BBTools.utils.RQCFilterRunner import RQCFilterRunner
from BBTools.utils.MemEstimatorRunner import MemEstimatorRunner
#END_HEADER


class BBTools:
    '''
    Module Name:
    BBTools

    Module Description:

    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.4.6"
    GIT_URL = "https://github.com/briehl/BBTools"
    GIT_COMMIT_HASH = "0e7df3fdbe0dceaff7271827f7fd77a855776676"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.scratch_dir = os.path.abspath(config['scratch'])
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        #END_CONSTRUCTOR
        pass


    def run_RQCFilter_app(self, ctx, io_params, run_params):
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
           servers for processing), barcodefilter=f, and mapk=13. Notes below
           are taken from the help output from rqcfilter2.sh ver 38.00
           Parameters (format = param name - default - description):
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
           in the app, as a file in local function) Memory requirements
           (DON'T EXPOSE THESE TO APPS):
           ------------------------------------------------- maxmem - 50 -
           Set maximum memory flag for RQCFilter to try to allocate. Should
           be an integer, in GB.) -> structure: parameter "library" of
           String, parameter "trimfragadapter" of type "boolean" (A boolean -
           0 for false, 1 for true. @range (0, 1)), parameter "qtrim" of
           String, parameter "trimq" of Long, parameter "maxns" of Long,
           parameter "minavgquality" of Long, parameter "minlength" of Long,
           parameter "mlf" of Double, parameter "removemouse" of type
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
           @range (0, 1)), parameter "maxmem" of Long
        :returns: instance of type "RQCFilterAppOutput" -> structure:
           parameter "report_name" of String, parameter "report_ref" of
           String, parameter "run_command" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_RQCFilter_app
        rqcfilter = RQCFilterRunner(self.callback_url, self.scratch_dir)
        output = rqcfilter.run_app(io_params, run_params)
        #END run_RQCFilter_app

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_RQCFilter_app return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def run_RQCFilter_local(self, ctx, io_params, run_params):
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
           servers for processing), barcodefilter=f, and mapk=13. Notes below
           are taken from the help output from rqcfilter2.sh ver 38.00
           Parameters (format = param name - default - description):
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
           in the app, as a file in local function) Memory requirements
           (DON'T EXPOSE THESE TO APPS):
           ------------------------------------------------- maxmem - 50 -
           Set maximum memory flag for RQCFilter to try to allocate. Should
           be an integer, in GB.) -> structure: parameter "library" of
           String, parameter "trimfragadapter" of type "boolean" (A boolean -
           0 for false, 1 for true. @range (0, 1)), parameter "qtrim" of
           String, parameter "trimq" of Long, parameter "maxns" of Long,
           parameter "minavgquality" of Long, parameter "minlength" of Long,
           parameter "mlf" of Double, parameter "removemouse" of type
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
           @range (0, 1)), parameter "maxmem" of Long
        :returns: instance of type "RQCFilterLocalOutput" (The output from
           the local function version of RQCFilter. output_directory: the
           path to the output directory containing all files generated by
           RQCFilter. run_log: the path to the run log from RQCFilter (i.e.
           its stderr). This will be a path in the output directory, added
           separately here for convenience. filtered_fastq_file: the path to
           the file (in the output directory) containing the filtered FASTQ
           reads. This will likely be compressed, if you need it
           decompressed, you can use DataFileUtil.unpack_file (see that
           module). run_command: the string that's run on the command line
           with all parameters formatted, etc.) -> structure: parameter
           "output_directory" of String, parameter "run_log" of String,
           parameter "filtered_fastq_file" of String, parameter "run_command"
           of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_RQCFilter_local
        rqcfilter = RQCFilterRunner(self.callback_url, self.scratch_dir)
        output = rqcfilter.run_local(io_params, run_params)
        #END run_RQCFilter_local

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_RQCFilter_local return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def run_mem_estimator(self, ctx, params):
        """
        This is a local function that estimates how much memory SPAdes or metaSPAdes needs
        to assemble a paired end library.
        Returns a float, representing the estimated memory use in GB.
        :param params: instance of type "MemEstimatorParams" (reads_file -
           path to a paired end reads file. If this is here alone, expect it
           to be interleaved. reads_file2 - path to the pair of the first
           file.) -> structure: parameter "reads_file" of String, parameter
           "reads_file2" of String
        :returns: instance of type "MemEstimatorOutput" (estimate - the
           estimated amount of memory required to assemble the paired end
           files, in GB.) -> structure: parameter "estimate" of Double
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_mem_estimator
        runner = MemEstimatorRunner(params)
        result = runner.run()
        output = {
            "estimate": result
        }
        #END run_mem_estimator

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_mem_estimator return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def bbtools_version(self, ctx):
        """
        Returns the semantic version of the currently installed BBTools. So something like "38.08"
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: version
        #BEGIN bbtools_version
        version_file_path = "/kb/module/bbmap_version"
        if not os.path.exists(version_file_path):
            version = "unknown"
        else:
            with open(version_file_path, "r") as ver_file:
                version = ver_file.read().strip()
        #END bbtools_version

        # At some point might do deeper type checking...
        if not isinstance(version, basestring):
            raise ValueError('Method bbtools_version return value ' +
                             'version is not type basestring as required.')
        # return the results
        return [version]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
