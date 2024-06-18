#
# PySNMP MIB module Dell-SSL (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-SSL
# Produced by pysmi-0.3.4 at Mon Apr 29 18:41:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, iso, Integer32, Counter32, Unsigned32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, ObjectIdentity, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "iso", "Integer32", "Counter32", "Unsigned32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "TimeTicks")
TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
rlSsl = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 100))
rlSsl.setRevisions(('2003-09-21 00:00',))
if mibBuilder.loadTexts: rlSsl.setLastUpdated('200309210000Z')
if mibBuilder.loadTexts: rlSsl.setOrganization('Dell')
rlSslCertificateGenerationTable = MibTable((1, 3, 6, 1, 4, 1, 89, 100, 1), )
if mibBuilder.loadTexts: rlSslCertificateGenerationTable.setStatus('current')
rlSslCertificateGenerationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 100, 1, 1), ).setIndexNames((0, "Dell-SSL", "rlSslCertificateGenerationIndex"))
if mibBuilder.loadTexts: rlSslCertificateGenerationEntry.setStatus('current')
rlSslCertificateGenerationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationIndex.setStatus('current')
rlSslCertificateGenerationId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationId.setStatus('current')
rlSslCertificateGenerationCountryName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationCountryName.setStatus('current')
rlSslCertificateGenerationStateOrProvinceName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationStateOrProvinceName.setStatus('current')
rlSslCertificateGenerationLocalityName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationLocalityName.setStatus('current')
rlSslCertificateGenerationOrganizationName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationOrganizationName.setStatus('current')
rlSslCertificateGenerationOrganizationUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationOrganizationUnitName.setStatus('current')
rlSslCertificateGenerationCommonName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationCommonName.setStatus('current')
rlSslCertificateGenerationValidDays = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationValidDays.setStatus('current')
rlSslCertificateGenerationRsaKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(512, 2048))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationRsaKeyLength.setStatus('current')
rlSslCertificateGenerationPassphrase = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationPassphrase.setStatus('current')
rlSslCertificateGenerationAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("generateRsaKeyAndSelfSignedCertificate", 1), ("generateSelfSignedCertificate", 2), ("generatePkcs12", 3), ("generateCertificateRequest", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationAction.setStatus('current')
rlSslCertificateExportTable = MibTable((1, 3, 6, 1, 4, 1, 89, 100, 2), )
if mibBuilder.loadTexts: rlSslCertificateExportTable.setStatus('current')
rlSslCertificateExportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 100, 2, 1), ).setIndexNames((0, "Dell-SSL", "rlSslCertificateExportId"), (0, "Dell-SSL", "rlSslCertificateExportType"), (0, "Dell-SSL", "rlSslCertificateExportFragmentId"))
if mibBuilder.loadTexts: rlSslCertificateExportEntry.setStatus('current')
rlSslCertificateExportId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportId.setStatus('current')
rlSslCertificateExportType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("certificateRequestPemFormat", 1), ("certificatePemFormat", 2), ("certificateOpenSslFormat", 3), ("certificateAndKeyPkcs12", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportType.setStatus('current')
rlSslCertificateExportFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportFragmentId.setStatus('current')
rlSslCertificateExportFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportFragmentText.setStatus('current')
rlSslCertificateSave = MibScalar((1, 3, 6, 1, 4, 1, 89, 100, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateSave.setStatus('current')
rlSslCertificateSaveFormat = MibScalar((1, 3, 6, 1, 4, 1, 89, 100, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("x509", 1), ("pkcs12", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateSaveFormat.setStatus('current')
rlSslImportedPKCS12CertificatePassphrase = MibScalar((1, 3, 6, 1, 4, 1, 89, 100, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 96))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslImportedPKCS12CertificatePassphrase.setStatus('current')
rlSslCertificateImportTable = MibTable((1, 3, 6, 1, 4, 1, 89, 100, 6), )
if mibBuilder.loadTexts: rlSslCertificateImportTable.setStatus('current')
rlSslCertificateImportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 100, 6, 1), ).setIndexNames((0, "Dell-SSL", "rlSslCertificateImportId"), (0, "Dell-SSL", "rlSslCertificateImportFormat"), (0, "Dell-SSL", "rlSslCertificateImportFragmentId"))
if mibBuilder.loadTexts: rlSslCertificateImportEntry.setStatus('current')
rlSslCertificateImportId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportId.setStatus('current')
rlSslCertificateImportFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("x509", 1), ("pkcs12", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFormat.setStatus('current')
rlSslCertificateImportFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFragmentId.setStatus('current')
rlSslCertificateImportFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFragmentText.setStatus('current')
rlSslCertificateImportFragmentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFragmentStatus.setStatus('current')
rlSslSSLv2Enable = MibScalar((1, 3, 6, 1, 4, 1, 89, 100, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslSSLv2Enable.setStatus('current')
class RlSslPublicKeyAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rsa", 1), ("dsa", 2))

rlSslImportExportSelfKeyTable = MibTable((1, 3, 6, 1, 4, 1, 89, 100, 8), )
if mibBuilder.loadTexts: rlSslImportExportSelfKeyTable.setStatus('current')
rlSslImportExportSelfKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 100, 8, 1), ).setIndexNames((0, "Dell-SSL", "rlSslImportExportSelfKeyFormat"), (0, "Dell-SSL", "rlSslImportExportSelfKeyIndex"), (0, "Dell-SSL", "rlSslImportExportSelfKeyFragmentId"))
if mibBuilder.loadTexts: rlSslImportExportSelfKeyEntry.setStatus('current')
rlSslImportExportSelfKeyFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("uuencoded-format", 1))))
if mibBuilder.loadTexts: rlSslImportExportSelfKeyFormat.setStatus('current')
rlSslImportExportSelfKeyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 8, 1, 2), Integer32())
if mibBuilder.loadTexts: rlSslImportExportSelfKeyIndex.setStatus('current')
rlSslImportExportSelfKeyFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 8, 1, 3), Integer32())
if mibBuilder.loadTexts: rlSslImportExportSelfKeyFragmentId.setStatus('current')
rlSslImportExportSelfKeyAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 8, 1, 4), RlSslPublicKeyAlgorithm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslImportExportSelfKeyAlgorithm.setStatus('current')
rlSslImportExportSelfKeyFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 8, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslImportExportSelfKeyFragmentText.setStatus('current')
rlSslCertificateSave2 = MibScalar((1, 3, 6, 1, 4, 1, 89, 100, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateSave2.setStatus('current')
rlSslisCertificate1Default = MibScalar((1, 3, 6, 1, 4, 1, 89, 100, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslisCertificate1Default.setStatus('current')
rlSslisCertificate2Default = MibScalar((1, 3, 6, 1, 4, 1, 89, 100, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslisCertificate2Default.setStatus('current')
mibBuilder.exportSymbols("Dell-SSL", rlSslisCertificate1Default=rlSslisCertificate1Default, rlSslCertificateGenerationOrganizationName=rlSslCertificateGenerationOrganizationName, rlSslCertificateImportFormat=rlSslCertificateImportFormat, rlSslCertificateSave2=rlSslCertificateSave2, PYSNMP_MODULE_ID=rlSsl, rlSslCertificateGenerationCommonName=rlSslCertificateGenerationCommonName, rlSslImportExportSelfKeyFragmentId=rlSslImportExportSelfKeyFragmentId, RlSslPublicKeyAlgorithm=RlSslPublicKeyAlgorithm, rlSslImportedPKCS12CertificatePassphrase=rlSslImportedPKCS12CertificatePassphrase, rlSslImportExportSelfKeyTable=rlSslImportExportSelfKeyTable, rlSslImportExportSelfKeyEntry=rlSslImportExportSelfKeyEntry, rlSslCertificateGenerationPassphrase=rlSslCertificateGenerationPassphrase, rlSslCertificateSaveFormat=rlSslCertificateSaveFormat, rlSslisCertificate2Default=rlSslisCertificate2Default, rlSslCertificateExportType=rlSslCertificateExportType, rlSslCertificateGenerationCountryName=rlSslCertificateGenerationCountryName, rlSslImportExportSelfKeyAlgorithm=rlSslImportExportSelfKeyAlgorithm, rlSslCertificateGenerationRsaKeyLength=rlSslCertificateGenerationRsaKeyLength, rlSslCertificateImportId=rlSslCertificateImportId, rlSslSSLv2Enable=rlSslSSLv2Enable, rlSslCertificateExportTable=rlSslCertificateExportTable, rlSslCertificateImportFragmentId=rlSslCertificateImportFragmentId, rlSslCertificateGenerationEntry=rlSslCertificateGenerationEntry, rlSslCertificateGenerationOrganizationUnitName=rlSslCertificateGenerationOrganizationUnitName, rlSslImportExportSelfKeyFragmentText=rlSslImportExportSelfKeyFragmentText, rlSslCertificateGenerationTable=rlSslCertificateGenerationTable, rlSslCertificateGenerationId=rlSslCertificateGenerationId, rlSslCertificateImportEntry=rlSslCertificateImportEntry, rlSslCertificateGenerationAction=rlSslCertificateGenerationAction, rlSslCertificateExportId=rlSslCertificateExportId, rlSslCertificateImportFragmentText=rlSslCertificateImportFragmentText, rlSslCertificateGenerationIndex=rlSslCertificateGenerationIndex, rlSslCertificateImportTable=rlSslCertificateImportTable, rlSslCertificateImportFragmentStatus=rlSslCertificateImportFragmentStatus, rlSsl=rlSsl, rlSslCertificateExportFragmentText=rlSslCertificateExportFragmentText, rlSslCertificateSave=rlSslCertificateSave, rlSslCertificateGenerationStateOrProvinceName=rlSslCertificateGenerationStateOrProvinceName, rlSslImportExportSelfKeyIndex=rlSslImportExportSelfKeyIndex, rlSslCertificateGenerationLocalityName=rlSslCertificateGenerationLocalityName, rlSslCertificateGenerationValidDays=rlSslCertificateGenerationValidDays, rlSslCertificateExportEntry=rlSslCertificateExportEntry, rlSslCertificateExportFragmentId=rlSslCertificateExportFragmentId, rlSslImportExportSelfKeyFormat=rlSslImportExportSelfKeyFormat)
