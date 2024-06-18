#
# PySNMP MIB module PDN-REACHDSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-REACHDSL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_interfaces, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-interfaces")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, iso, Bits, Integer32, TimeTicks, IpAddress, Counter32, ModuleIdentity, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Bits", "Integer32", "TimeTicks", "IpAddress", "Counter32", "ModuleIdentity", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdnReachDSL = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20))
pdnReachDSL.setRevisions(('2003-01-15 12:00', '2003-01-12 12:00', '2002-10-15 17:00', '2002-07-12 03:15',))
if mibBuilder.loadTexts: pdnReachDSL.setLastUpdated('200210151700Z')
if mibBuilder.loadTexts: pdnReachDSL.setOrganization('Paradyne Corp MIB Working Group')
pdnReachDSLObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1))
reachDSLSpectrumMgmtSelection = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtSelection.setStatus('current')
reachDSLSpectrumMgmtZone = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("usa1", 1), ("uk1", 2), ("canada1", 3), ("japan1", 4), ("emea1", 5))).clone('usa1')).setMaxAccess("readonly")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtZone.setStatus('deprecated')
reachDSLSpectrumMgmtConfTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 3), )
if mibBuilder.loadTexts: reachDSLSpectrumMgmtConfTable.setStatus('current')
reachDSLSpectrumMgmtConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: reachDSLSpectrumMgmtConfEntry.setStatus('current')
reachDSLSpectrumMgmtConfEWL = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtConfEWL.setStatus('current')
reachDSLSpectrumMgmtConfLoopLength = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("short", 1), ("medium", 2), ("long", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtConfLoopLength.setStatus('current')
reachDSLSpectrumMgmtConfAtucMaxTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-140, 120))).setUnits('tenth dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtConfAtucMaxTxPower.setStatus('current')
reachDSLSpectrumMgmtConfAturMaxTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-140, 120))).setUnits('tenth dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtConfAturMaxTxPower.setStatus('current')
reachDSLSpectrumMgmtConfQuadMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sameQuad", 1), ("segregatedQuadUpto3km", 2), ("segregatedQuadAbove3km", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtConfQuadMode.setStatus('current')
reachDSLSpectrumMgmtLineInfoTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4), )
if mibBuilder.loadTexts: reachDSLSpectrumMgmtLineInfoTable.setStatus('current')
reachDSLSpectrumMgmtLineInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: reachDSLSpectrumMgmtLineInfoEntry.setStatus('current')
reachDSLSpectrumMgmtAtucMaxTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 1), Unsigned32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtAtucMaxTxRate.setStatus('current')
reachDSLSpectrumMgmtAtucMinTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 2), Unsigned32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtAtucMinTxRate.setStatus('current')
reachDSLSpectrumMgmtAtucMaxTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-140, 120))).setUnits('tenth dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtAtucMaxTxPower.setStatus('current')
reachDSLSpectrumMgmtAturMaxTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 4), Unsigned32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtAturMaxTxRate.setStatus('current')
reachDSLSpectrumMgmtAturMinTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 5), Unsigned32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtAturMinTxRate.setStatus('current')
reachDSLSpectrumMgmtAturMaxTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-140, 120))).setUnits('tenth dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtAturMaxTxPower.setStatus('current')
reachDSLSpectrumMgmtMinEWL = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtMinEWL.setStatus('current')
reachDSLSpectrumMgmtMaxEWL = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtMaxEWL.setStatus('current')
reachDSLLineTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 5), )
if mibBuilder.loadTexts: reachDSLLineTable.setStatus('current')
reachDSLLineEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: reachDSLLineEntry.setStatus('current')
reachDSLPotsDetectionVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 74)).clone(3)).setUnits('volts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: reachDSLPotsDetectionVoltage.setStatus('current')
reachDSLCircuitIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: reachDSLCircuitIdentifier.setStatus('deprecated')
reachDSLSpectrumMgmtLoopMeasurementMethod = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("loopLength", 2), ("ewl", 3), ("quadMode", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtLoopMeasurementMethod.setStatus('current')
reachDSLSpectrumMgmtEWLUnits = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("feet", 2), ("meters", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtEWLUnits.setStatus('current')
reachDSLSpectrumMgmtMode = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enableOnly", 1), ("disableOnly", 2), ("both", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reachDSLSpectrumMgmtMode.setStatus('current')
pdnReachDSLConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2))
pdnReachDSLGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1))
pdnReachDSLCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 2))
pdnReachDSLCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 2, 2)).setObjects(("PDN-REACHDSL-MIB", "pdnReachDSLGeneralConfigGroup"), ("PDN-REACHDSL-MIB", "pdnReachDSLGeneralInformationGroup"), ("PDN-REACHDSL-MIB", "pdnReachDSLEWLModeGroup"), ("PDN-REACHDSL-MIB", "pdnReachDSLLoopLengthModeGroup"), ("PDN-REACHDSL-MIB", "pdnReachDSLQuadModeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnReachDSLCompliance1 = pdnReachDSLCompliance1.setStatus('current')
pdnReachDSLGeneralConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 4)).setObjects(("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtSelection"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfAtucMaxTxPower"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfAturMaxTxPower"), ("PDN-REACHDSL-MIB", "reachDSLPotsDetectionVoltage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnReachDSLGeneralConfigGroup = pdnReachDSLGeneralConfigGroup.setStatus('current')
pdnReachDSLGeneralInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 5)).setObjects(("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAtucMaxTxRate"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAtucMinTxRate"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAtucMaxTxPower"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAturMaxTxRate"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAturMinTxRate"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAturMaxTxPower"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtLoopMeasurementMethod"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtEWLUnits"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnReachDSLGeneralInformationGroup = pdnReachDSLGeneralInformationGroup.setStatus('current')
pdnReachDSLEWLModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 6)).setObjects(("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfEWL"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtMinEWL"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtMaxEWL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnReachDSLEWLModeGroup = pdnReachDSLEWLModeGroup.setStatus('current')
pdnReachDSLLoopLengthModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 7)).setObjects(("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfLoopLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnReachDSLLoopLengthModeGroup = pdnReachDSLLoopLengthModeGroup.setStatus('current')
pdnReachDSLQuadModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 8)).setObjects(("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfQuadMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnReachDSLQuadModeGroup = pdnReachDSLQuadModeGroup.setStatus('current')
pdnReachDSLCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 2, 1)).setObjects(("PDN-REACHDSL-MIB", "pdnReachDSLConfigurationGroup"), ("PDN-REACHDSL-MIB", "pdnReachDSLInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnReachDSLCompliance = pdnReachDSLCompliance.setStatus('deprecated')
pdnReachDSLConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 1)).setObjects(("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtSelection"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfEWL"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfLoopLength"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfAtucMaxTxPower"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfAturMaxTxPower"), ("PDN-REACHDSL-MIB", "reachDSLPotsDetectionVoltage"), ("PDN-REACHDSL-MIB", "reachDSLCircuitIdentifier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnReachDSLConfigurationGroup = pdnReachDSLConfigurationGroup.setStatus('deprecated')
pdnReachDSLInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 2)).setObjects(("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAtucMaxTxRate"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAtucMinTxRate"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAtucMaxTxPower"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAturMaxTxRate"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAturMinTxRate"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAturMaxTxPower"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtMinEWL"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtMaxEWL"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtLoopMeasurementMethod"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtEWLUnits"), ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnReachDSLInformationGroup = pdnReachDSLInformationGroup.setStatus('deprecated')
pdnReachDSLDeprecatedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 3)).setObjects(("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtZone"), ("PDN-REACHDSL-MIB", "reachDSLCircuitIdentifier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnReachDSLDeprecatedGroup = pdnReachDSLDeprecatedGroup.setStatus('deprecated')
mibBuilder.exportSymbols("PDN-REACHDSL-MIB", pdnReachDSLGeneralConfigGroup=pdnReachDSLGeneralConfigGroup, reachDSLSpectrumMgmtEWLUnits=reachDSLSpectrumMgmtEWLUnits, pdnReachDSLCompliance=pdnReachDSLCompliance, reachDSLSpectrumMgmtAtucMaxTxPower=reachDSLSpectrumMgmtAtucMaxTxPower, reachDSLSpectrumMgmtMaxEWL=reachDSLSpectrumMgmtMaxEWL, pdnReachDSLLoopLengthModeGroup=pdnReachDSLLoopLengthModeGroup, reachDSLSpectrumMgmtConfAtucMaxTxPower=reachDSLSpectrumMgmtConfAtucMaxTxPower, reachDSLSpectrumMgmtConfEntry=reachDSLSpectrumMgmtConfEntry, reachDSLPotsDetectionVoltage=reachDSLPotsDetectionVoltage, pdnReachDSLConformance=pdnReachDSLConformance, reachDSLSpectrumMgmtZone=reachDSLSpectrumMgmtZone, reachDSLCircuitIdentifier=reachDSLCircuitIdentifier, reachDSLSpectrumMgmtMode=reachDSLSpectrumMgmtMode, pdnReachDSLQuadModeGroup=pdnReachDSLQuadModeGroup, reachDSLSpectrumMgmtConfEWL=reachDSLSpectrumMgmtConfEWL, reachDSLSpectrumMgmtAtucMaxTxRate=reachDSLSpectrumMgmtAtucMaxTxRate, reachDSLSpectrumMgmtConfQuadMode=reachDSLSpectrumMgmtConfQuadMode, reachDSLSpectrumMgmtAtucMinTxRate=reachDSLSpectrumMgmtAtucMinTxRate, pdnReachDSLDeprecatedGroup=pdnReachDSLDeprecatedGroup, reachDSLSpectrumMgmtLoopMeasurementMethod=reachDSLSpectrumMgmtLoopMeasurementMethod, pdnReachDSLCompliances=pdnReachDSLCompliances, pdnReachDSLConfigurationGroup=pdnReachDSLConfigurationGroup, PYSNMP_MODULE_ID=pdnReachDSL, pdnReachDSLObjects=pdnReachDSLObjects, reachDSLSpectrumMgmtConfTable=reachDSLSpectrumMgmtConfTable, pdnReachDSLGroups=pdnReachDSLGroups, pdnReachDSLEWLModeGroup=pdnReachDSLEWLModeGroup, pdnReachDSL=pdnReachDSL, reachDSLSpectrumMgmtAturMaxTxRate=reachDSLSpectrumMgmtAturMaxTxRate, reachDSLSpectrumMgmtLineInfoTable=reachDSLSpectrumMgmtLineInfoTable, reachDSLLineTable=reachDSLLineTable, reachDSLSpectrumMgmtConfAturMaxTxPower=reachDSLSpectrumMgmtConfAturMaxTxPower, reachDSLSpectrumMgmtSelection=reachDSLSpectrumMgmtSelection, reachDSLSpectrumMgmtLineInfoEntry=reachDSLSpectrumMgmtLineInfoEntry, pdnReachDSLInformationGroup=pdnReachDSLInformationGroup, reachDSLSpectrumMgmtMinEWL=reachDSLSpectrumMgmtMinEWL, reachDSLLineEntry=reachDSLLineEntry, reachDSLSpectrumMgmtAturMaxTxPower=reachDSLSpectrumMgmtAturMaxTxPower, reachDSLSpectrumMgmtConfLoopLength=reachDSLSpectrumMgmtConfLoopLength, pdnReachDSLCompliance1=pdnReachDSLCompliance1, pdnReachDSLGeneralInformationGroup=pdnReachDSLGeneralInformationGroup, reachDSLSpectrumMgmtAturMinTxRate=reachDSLSpectrumMgmtAturMinTxRate)
