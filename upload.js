import { NFTStorage } from 'nft.storage';
import { filesFromPaths } from 'files-from-path';
import { globby } from 'globby';
import path from 'path';

async function main() {
  const paths = await globby([
    'innovations/**/*.*',       // match all files recursively
    '!**/.DS_Store',            // ignore MacOS metadata
    '!**/node_modules/**',      // optional: ignore dependencies
  ]);

  if (paths.length === 0) {
    console.error('❌ No files matched in innovations/, aborting upload.');
    process.exit(1);
  }

  const files = await filesFromPaths(paths);
  console.log(`📦 Uploading ${files.length} files...`);

  const client = new NFTStorage({ token: process.env.NFT_STORAGE_API_TOKEN });
  const cid = await client.storeDirectory(files);

  console.log('✅ Uploaded folder with CID:', cid);
  console.log(`🔗 https://nftstorage.link/ipfs/${cid}`);
}

main().catch(err => {
  console.error('❌ Upload failed:', err.message || err);
  console.error(err.stack);
  process.exit(1);
});
