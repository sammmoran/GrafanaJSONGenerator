local grafana = import "../grafonnet-lib/grafonnet/grafana.libsonnet";
local dashboard = grafana.dashboard;
local row = grafana.row;
local singlestat = grafana.singlestat;
local cloudwatch = grafana.cloudwatch;
local template = grafana.template;

dashboard.new("cip-service")
.addTemplate(
	grafana.template.datasource(
	'cip-service-ds',
	'cloudwatch',
	'CloudWatch',
	)
)
.addPanel(
	singlestat.new(
		'uptime',
		formate='s',
		datasource='CloudWatch',
		span=2,
	),
	gridPos={
		x:0,
		y:0,
		w:24,
		h:3,
	}
)