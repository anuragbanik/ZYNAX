export function isMigrationFile(fileName) {
  return /^\d+.*\.sql$/.test(fileName);
}
