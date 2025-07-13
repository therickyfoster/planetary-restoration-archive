import { NFTStorage } from 'nft.storage';
import { filesFromPaths } from 'files-from-path';
import globby from 'globby';

async function main() {
  const paths = await globby([
    'public/**',           // Only upload the "public" folder
    '!public/**/*.map',    // (Optional) exclude sourcemaps
    '!public/**/.DS_Store' // (Optional) exclude junk files
  ]);

  const files = await filesFromPaths(paths);

  const client = new NFTStorage({
    token: process.env.NFT_STORAGE_API_TOKEN
  });

  const cid = await client.storeDirectory(files);
  console.log('✅ Uploaded folder with CID:', cid);
}

main().catch(err => {
  console.error('❌ Upload failed:', err.message || err);
  console.error(err.stack);
  process.exit(1);
});
