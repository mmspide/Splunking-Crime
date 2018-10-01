#   Version 7.0.2
#
# This file contains possible attribute/value pairs for saved search entries in
# savedsearches.conf.  You can configure saved searches by creating your own
# savedsearches.conf.
#
# There is the default savedsearches.conf in $SPLUNK_HOME/etc/apps/Splunk_ML_Toolkit/default. To
# set custom configurations, place a savedsearches.conf in
# $SPLUNK_HOME/etc/apps/Splunk_ML_Toolkit/local/.  You must restart Splunk to enable configurations.
#
# To learn more about configuration files (including precedence) please see the
# documentation located at
# http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles

[default]
args.mltk.experiment = [0|1]
* default to false
* If it sets to true, the saved search is a MLTK experiment type of saved search (schedule training or alert).

args.mltk.experiment.title = <string>
* A human readable title of experiment type of saved search, since the original 'name' field is set to uuid.

args.mltk.experiment.alert.type = <string>
* required
* the type of alert generated by applying a model
* possible values: 
*   NumericValue, CategoricalOutlierCount, CategoricalValue, ClusterEventCount, NumericOutlierCount:

args.mltk.experiment.alert.field = <string>
* the field produced by applying the algorithm used in the comparision
* available in NumericValue, CategoricalValue

args.mltk.experiment.alert.comparator = <string>
* the operator to use
* available in NumericValue, CategoricalValue, ClusterEventCount, NumericOutlierCount

args.mltk.experiment.alert.firstValue = <int>
* the value to compare to the selected field
* available in NumericValue

args.mltk.experiment.alert.secondValue = <int>
* the value to compare to if the operator requires a second value
* available in NumericValue

args.mltk.experiment.alert.probableCauseFields = <string>
* a list of field names encoded in JSON
* available in CategoricalOutlierCount

args.mltk.experiment.alert.values = <string>
* a list of values encoded in JSON
* available in CategoricalValue

args.mltk.experiment.alert.clusterId = <string>
* available in ClusterEventCount

args.mltk.experiment.alert.firstCount = <int>
* available in ClusterEventCount

args.mltk.experiment.alert.secondCount = <int>
* available in ClusterEventCount