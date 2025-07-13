import { NFTStorage } from 'nft.storage';
import { filesFromPaths } from 'files-from-path';
import { globby } from 'globby'; // ✅ FIXED
import path from 'path';

async function main() {
  const paths = await globby([
    'public/**',
    '!public/**/*.map',
    '!public/**/.DS_Store'
  ]);

  const files = await filesFromPaths(paths);

  const client = new NFTStorage({ token: process.env.NFT_STORAGE_API_TOKEN });
  const cid = await client.storeDirectory(files);

  console.log('✅ Uploaded folder with CID:', cid);
}

main().catch(err => {
  console.error('❌ Upload failed:', err.message || err);
  console.error(err.stack);
  process.exit(1);
});
